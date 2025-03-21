INSERT INTO zone (zone_name) VALUES
('Bogotá'),
('Medellín'),
('Cali'),
('Barranquilla'),
('Cartagena'),
('Bucaramanga'),
('Pereira'),
('Cúcuta'),
('Santa Marta'),
('Manizales');

INSERT INTO area (area_name, zone_id) VALUES
('Historic Center', 1),
('Financial District', 1),
('Downtown', 2),
('Residential Area', 2),
('Beachfront', 3),
('Tourist Zone', 3),
('University Campus', 4),
('Technology Park', 4),
('Industrial Zone', 5),
('Shopping Mall Area', 5),
('Cultural District', 6),
('Entertainment Hub', 6),
('Medical District', 7),
('Sports Complex', 7),
('Green Park', 8),
('Residential Towers', 8),
('Harbor Area', 9),
('Old Town', 9),
('Airport Zone', 10),
('Business Center', 10);

INSERT INTO user (name, user_email, mobile_number, area_id, user_type, description, verification_code) VALUES
('Alice Johnson', 'alice.johnson@example.com', '3001234567', 1, 'CUSTOMER', 'Frequent customer looking for discounts', 1234),
('Bob Smith', 'bob.smith@example.com', '3102345678', 2, 'DELIVERY', NULL, 1234),
('Charlie Brown', 'charlie.brown@example.com', '3203456789', 3, 'STORE', NULL, 1234),
('Diana Ross', 'diana.ross@example.com', '3304567890', 4, 'CUSTOMER', 'Loyal customer of organic products', 1234),
('Ethan Hunt', 'ethan.hunt@example.com', '3405678901', 5, 'DELIVERY', NULL, 1234),
('Fiona Adams', 'fiona.adams@example.com', '3506789012', 6, 'STORE', NULL, 1234),
('George Martin', 'george.martin@example.com', '3607890123', 7, 'CUSTOMER', 'Interested in new tech gadgets', 1234),
('Helen Carter', 'helen.carter@example.com', '3708901234', 8, 'DELIVERY', NULL, 1234),
('Ian Wright', 'ian.wright@example.com', '3809012345', 9, 'STORE', NULL, 1234),
('Jack Daniels', 'jack.daniels@example.com', '3900123456', 10, 'CUSTOMER', 'Wine collector and enthusiast', 1234);

INSERT INTO store (nit, name, address, longitude, latitude, logo) VALUES
('900123456-1', 'Tech Haven', '123 Tech Street, Bogotá', -74.0721, 4.7110, 'https://example.com/logo1.png'),
('900987654-2', 'Food Express', '456 Market Ave, Medellín', -75.5640, 6.2518, 'https://example.com/logo2.png'),
('901234567-3', 'Gadget World', '789 Innovation Blvd, Cali', -76.5320, 3.4516, 'https://example.com/logo3.png'),
('901876543-4', 'Organic Market', '321 Fresh Lane, Barranquilla', -74.7964, 10.9639, 'https://example.com/logo4.png'),
('902345678-5', 'Book Haven', '654 Library St, Cartagena', -75.5144, 10.3997, 'https://example.com/logo5.png'),
('902987654-6', 'Fashion Hub', '987 Trendy Ave, Bucaramanga', -73.1198, 7.1254, 'https://example.com/logo6.png'),
('903456789-7', 'Home Essentials', '741 Comfort Rd, Manizales', -75.5138, 5.0703, 'https://example.com/logo7.png'),
('903876543-8', 'Fitness Gear', '852 Gym St, Pereira', -75.6961, 4.8143, 'https://example.com/logo8.png'),
('904567890-9', 'Coffee Lovers', '963 Java Ave, Armenia', -75.6795, 4.5339, 'https://example.com/logo9.png'),
('904987654-10', 'ElectroWorld', '258 Electric St, Cúcuta', -72.5078, 7.8939, 'https://example.com/logo10.png');

insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('8th Floor', 4.7541706271, 'https://picsum.photos/350', -74.08625703, 'Nlounge', 340167108, 11);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Suite 98', 4.7808241926, 'https://picsum.photos/350', -74.0438694246, 'Jaxnation', 712253978, 12);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('12th Floor', 4.7717550465, 'https://picsum.photos/350', -74.1111937384, 'Topicstorm', 560394616, 13);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Suite 34', 4.7470401245, 'https://picsum.photos/350', -74.0438694246, 'Photofeed', 586554260, 14);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Apt 1129', 4.8058962677, 'https://picsum.photos/350', -74.058454808, 'Teklist', 172978945, 15);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('PO Box 22324', 4.7654601425, 'https://picsum.photos/350', -74.0707640695, 'Buzzbean', 661672420, 16);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Apt 1501', 4.8174776639, 'https://picsum.photos/350', -74.0407268455, 'Talane', 732621049, 17);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('PO Box 91366', 4.7830556603, 'https://picsum.photos/350', -74.0981548962, 'Topicblab', 884841226, 18);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('8th Floor', 4.8364426635, 'https://picsum.photos/350', -74.0306918478, 'Youtags', 661879279, 19);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Suite 98', 4.7712460899, 'https://picsum.photos/350', -74.0383699113, 'Zooveo', 739218345, 20);

--Girardot
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('PO Box 85294', 4.2969263821, 'https://picsum.photos/350', -74.7718930335, 'Abata', 520471467, 21);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Room 148', 4.3028783578, 'https://picsum.photos/350', -74.7653507909, 'Meeveo', 364727056, 22);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('15th Floor', 4.2829441305, 'https://picsum.photos/350', -74.7718930335, 'Livetube', 625556943, 23);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Suite 57', 4.2885973859, 'https://picsum.photos/350', -74.7737801137, 'Livefish', 799782206, 24);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('PO Box 3128', 4.2885973859, 'https://picsum.photos/350', -74.7896346988, 'Dabjam', 379779448, 25);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Apt 715', 4.2896921518, 'https://picsum.photos/350', -74.7718930335, 'Devify', 700376435, 26);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Suite 14', 4.2820275539, 'https://picsum.photos/350', -74.7932030414, 'InnoZ', 861930917, 27);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('PO Box 52306', 4.2885973859, 'https://picsum.photos/350', -74.7551772758, 'Realblab', 825152494, 28);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Suite 17', 4.2885973859, 'https://picsum.photos/350', -74.755523475, 'Youbridge', 976902595, 29);
insert into STORE (address, latitude, logo, longitude, name, nit, store_id ) values ('Suite 3', 4.3146284448, 'https://picsum.photos/350', -74.7761234576, 'Kwilith', 734885095, 30);

UPDATE store
SET logo = 'https://picsum.photos/350';

INSERT INTO user_store (user_id, store_id) VALUES
(3, 1),
(3, 2),
(3, 3),
(3, 4),
(3, 5),
(6, 6),
(6, 7),
(6, 8),
(9, 9),
(9, 10);

INSERT INTO product (store_id, name, product_type, unit_price, detail, score, image) VALUES
(1, 'Smartphone X', 'PRODUCT', 799.99, 'Latest generation smartphone with AI features', 4.5, 'https://example.com/smartphone.png'),
(2, 'Gourmet Coffee Subscription', 'SUBSCRIPTION', 19.99, 'Monthly delivery of premium coffee beans', 4.8, 'https://example.com/coffee.png'),
(3, 'Gaming Laptop', 'PRODUCT', 1299.99, 'Powerful laptop for gaming and productivity', 4.6, 'https://example.com/laptop.png'),
(4, 'Organic Vegetables', 'PRODUCT', 24.99, 'Fresh organic vegetables delivered weekly', 4.7, 'https://example.com/veggies.png'),
(5, 'Streaming Service Subscription', 'SUBSCRIPTION', 14.99, 'Unlimited movies and TV shows', 4.3, 'https://example.com/streaming.png'),
(6, 'Running Shoes', 'PRODUCT', 89.99, 'Lightweight and comfortable running shoes', 4.5, 'https://example.com/shoes.png'),
(7, 'Meal Prep Subscription', 'SUBSCRIPTION', 49.99, 'Healthy meals delivered to your door', 4.9, 'https://example.com/meals.png'),
(8, 'Wireless Earbuds', 'PRODUCT', 129.99, 'Noise-canceling earbuds with Bluetooth 5.0', 4.6, 'https://example.com/earbuds.png'),
(9, 'Monthly Gym Membership', 'SUBSCRIPTION', 39.99, 'Access to all gym facilities and classes', 4.4, 'https://example.com/gym.png'),
(10, 'E-Book Reader', 'PRODUCT', 199.99, 'High-resolution e-ink display for reading books', 4.7, 'https://example.com/ebook.png');

INSERT INTO user_subscription (product_id, user_id, subscription_type, start_date, end_date) VALUES
    (5, 1, 'MONTH', date('now'), date('now', '+30 days')),
    (7, 1, 'YEAR', date('now'), date('now', '+365 days')),
    (5, 4, 'MONTH', date('now'), date('now', '+30 days')),
    (7, 4, 'YEAR', date('now'), date('now', '+365 days'));

INSERT INTO product_tag (product_id, value) VALUES
(1, '150g'),
(1, 'Organic'),
(1, 'Gluten-Free'),
(1, 'Vegan'),
(1, 'Low Fat'),

(2, '1L'),
(2, 'Sugar-Free'),
(2, 'Imported'),
(2, 'Eco-Friendly'),
(2, 'Non-GMO'),

(3, '500ml'),
(3, 'Handmade'),
(3, 'BPA-Free'),
(3, 'Dairy-Free'),
(3, 'No Preservatives'),

(4, '250g'),
(4, 'High Protein'),
(4, 'Artisanal'),
(4, 'Zero Sugar'),
(4, 'Soy-Free'),

(5, '6-pack'),
(5, 'Locally Sourced'),
(5, 'Preservative-Free'),
(5, 'Sustainable'),
(5, 'Cold-Pressed'),

(6, '2kg'),
(6, 'Low Carb'),
(6, 'Hormone-Free'),
(6, 'Organic Certified'),
(6, 'Farm Fresh'),

(7, '300g'),
(7, 'Gluten-Free'),
(7, 'Vegan'),
(7, 'Non-GMO'),
(7, 'No Artificial Colors'),

(8, '750ml'),
(8, 'Artisan'),
(8, 'Eco-Packaging'),
(8, 'Premium Quality'),
(8, 'Recyclable'),

(9, '200g'),
(9, 'Kosher'),
(9, 'Halal'),
(9, 'No Additives'),
(9, 'Heart Healthy'),

(10, '5kg'),
(10, 'High Fiber');

INSERT INTO user_rating (product_id, user_id, score) VALUES
(1, 1, 4),
(1, 2, 3),
(1, 3, 5),
(2, 4, 2),
(2, 5, 4),
(2, 6, 3),
(3, 7, 5),
(3, 8, 4),
(3, 9, 3),
(4, 10, 2),
(4, 1, 4),
(5, 2, 3),
(5, 3, 4),
(5, 4, 5),
(6, 5, 2),
(6, 6, 3),
(7, 7, 4),
(7, 8, 3),
(8, 9, 2),
(8, 10, 4),
(9, 1, 3),
(9, 2, 5),
(10, 3, 4),
(10, 4, 3),
(10, 5, 4);

INSERT INTO cart (user_id, creation_date, status, status_date) VALUES
(1, DATE('now', '-1 day'), 'ACTIVE', DATE('now')),
(2, DATE('now', '-2 day'), 'PAYMENT_PROGRESS', DATE('now', '-1 day')),
(3, DATE('now', '-3 days'), 'BILLED', DATE('now', '-2 days')),
(4, DATE('now', '-4 days'), 'DISABLED', DATE('now', '-3 days')),
(5, DATE('now', '-5 days'), 'ACTIVE', DATE('now', '-4 days')),
(6, DATE('now', '-6 days'), 'PAYMENT_PROGRESS', DATE('now', '-5 days')),
(7, DATE('now', '-7 days'), 'BILLED', DATE('now', '-6 days')),
(8, DATE('now', '-8 days'), 'DISABLED', DATE('now', '-7 days')),
(9, DATE('now', '-9 days'), 'ACTIVE', DATE('now', '-8 days')),
(10, DATE('now', '-10 days'), 'PAYMENT_PROGRESS', DATE('now', '-9 days'));

INSERT INTO cart_product (cart_id, product_id, quantity) VALUES
(1, 1, 2),
(1, 2, 1),
(1, 3, 4),
(2, 4, 1),
(2, 5, 3),
(3, 6, 2),
(3, 7, 5),
(4, 8, 1),
(4, 9, 3),
(5, 10, 2),
(6, 1, 4),
(6, 2, 1),
(7, 3, 2),
(7, 4, 3),
(8, 5, 1),
(8, 6, 2),
(9, 7, 4),
(9, 8, 3),
(10, 9, 2),
(10, 10, 5),
(11, 1, 1),
(11, 2, 3),
(11, 3, 2),
(11, 4, 1);

INSERT INTO user_order (user_id, cart_id, creation_date, status, billed_date, total_price) VALUES
(1, 1, '2025-03-13', 'ACTIVE', NULL, 59.99),
(2, 2, '2025-03-13', 'PAYMENT_PROGRESS', NULL, 89.50),
(3, 3, '2025-03-13', 'BILLED', '2025-03-14', 120.75),
(4, 4, '2025-03-13', 'BILLED', '2025-03-14', 45.25),
(5, 5, '2025-03-13', 'DISABLED', NULL, 67.80),
(6, 6, '2025-03-13', 'ACTIVE', NULL, 99.99),
(7, 7, '2025-03-13', 'PAYMENT_PROGRESS', NULL, 150.00),
(8, 8, '2025-03-13', 'BILLED', '2025-03-14', 200.45),
(9, 9, '2025-03-13', 'BILLED', '2025-03-14', 25.60),
(10, 10, '2025-03-13', 'PAYMENT_DECLINED', NULL, 75.99),
(11, 11, '2025-03-13', 'ACTIVE', NULL, 99.99);