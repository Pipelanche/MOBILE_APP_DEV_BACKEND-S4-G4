from models.store import Store
from app import db
from math import radians, cos, sin, sqrt, atan2
from models.product import Product
from sqlalchemy import func, desc
from datetime import datetime

def get_all_stores():
    """Fetch all stores from the database."""
    return Store.query.all()

def get_store_by_id(store_id):
    """Fetch a single store by ID."""
    return Store.query.get(store_id)

def create_store(nit, name, address, longitude, latitude, logo, opens_at, closes_at):
    """Create a new store in the database."""
    # 1. Verificar conflicto de NIT
    existing = Store.query.filter_by(nit=nit).first()
    if existing:
        return {"error": "Store with this NIT already exists"}, 409

    # 2. Parsear los horarios si vienen como cadenas
    if isinstance(opens_at, str):
        opens_at = datetime.strptime(opens_at, "%H:%M:%S").time()
    if isinstance(closes_at, str):
        closes_at = datetime.strptime(closes_at, "%H:%M:%S").time()

    # 3. Crear instancia con keyword args
    new_store = Store(
        nit=nit,
        name=name,
        address=address,
        longitude=longitude,
        latitude=latitude,
        logo=logo,
        opens_at=opens_at,
        closes_at=closes_at
    )

    # 4. Persistir en la base
    db.session.add(new_store)
    db.session.commit()

    return new_store

def update_store(store_id, nit, name, address, longitude, latitude, opens_at, closes_at, logo=None):
    """Update an existing store."""
    store = Store.query.get(store_id)
    if not store:
        return None  # Store not found

    # Ensure NIT is unique
    existing_store = Store.query.filter(Store.nit == nit, Store.store_id != store_id).first()
    if existing_store:
        return {"error": "Store with this NIT already exists"}, 409  # Conflict error

    store.nit = nit
    store.name = name
    store.address = address
    store.longitude = longitude
    store.latitude = latitude
    if logo:
        store.logo = logo
  # Asegurarse de que longitud y latitud sean floats
    try:
        store.longitude = float(longitude)
        store.latitude = float(latitude)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Longitud o latitud inválida: {e}")
    
    # --- Convertir cadenas de hora a objetos datetime.time ---
    try:
        # Asumimos que opens_at y closes_at son cadenas en formato "HH:MM:SS"
        # Si el formato puede variar (ej. "HH:MM"), ajusta el string de formato.
        if isinstance(opens_at, str):
            store.opens_at = datetime.strptime(opens_at, '%H:%M:%S').time()
        elif isinstance(opens_at, time): # Si ya es un objeto time
            store.opens_at = opens_at
        else:
            raise ValueError("Formato de 'opens_at' inválido. Se esperaba una cadena HH:MM:SS o un objeto time.")

        if isinstance(closes_at, str):
            store.closes_at = datetime.strptime(closes_at, '%H:%M:%S').time()
        elif isinstance(closes_at, time): # Si ya es un objeto time
            store.closes_at = closes_at
        else:
            raise ValueError("Formato de 'closes_at' inválido. Se esperaba una cadena HH:MM:SS o un objeto time.")
            
    except ValueError as e:
        # Si el formato de la hora es incorrecto, strptime lanzará un ValueError.
        # Relanzamos como un error más específico o lo manejamos.
        raise ValueError(f"Formato de hora inválido. Asegúrate de que sea 'HH:MM:SS'. Detalle: {e}")

    store.updated_at = datetime.now()
    # Print store details as JSON
    print(store.name)
    db.session.commit()
    return store

def delete_store(store_id):
    """Delete a store from the database."""
    store = Store.query.get(store_id)
    if not store:
        return None  # Store not found

    db.session.delete(store)
    db.session.commit()
    return {"message": f"Store {store_id} deleted successfully"}

EARTH_RADIUS_KM = 6371  # Earth radius in kilometers

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two coordinates using Haversine formula."""
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS_KM * c  # Distance in kilometers

def get_nearby_stores(lat, lon, radius_km=5):
    """Find stores within a given radius (default: 5km)."""
    stores = Store.query.all()  # Fetch all stores from DB
    nearby_stores = []

    for store in stores:
        distance = calculate_distance(lat, lon, store.latitude, store.longitude)
        
        # ✅ Debugging print statement with type casting
        print(f"Store ID: {store.store_id} | Distance: {distance:.2f} km")
        
        if distance <= radius_km:
            nearby_stores.append(store)
    return nearby_stores

def get_top_valuable_stores(limit=3):
    """
    Return the top N stores with the most valuable products based on average score.
    Does not return product info, only store details.
    """
    top_stores = (
        db.session.query(Store)
        .join(Product, Store.store_id == Product.store_id)
        .group_by(Store.store_id)
        .order_by(desc(func.avg(Product.score)))
        .limit(limit)
        .all()
    )
    return top_stores