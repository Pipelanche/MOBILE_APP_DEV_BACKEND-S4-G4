from enum import Enum

class UserType(Enum):
    CUSTOMER = 'CUSTOMER'
    DELIVERY = 'DELIVERY'
    STORE = 'STORE'

class ProductType(Enum):
    PRODUCT = 'PRODUCT'
    SUBSCRIPTION = 'SUBSCRIPTION'

class SubscriptionType(Enum):
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    YEAR = 'YEAR'

class Status(Enum):
    ACTIVE = 'ACTIVE'
    PAYMENT_PROGRESS = 'PAYMENT_PROGRESS'
    PAYMENT_DECLINED = 'PAYMENT_DECLINED'
    BILLED = 'BILLED'
    DISABLED = 'DISABLED'
