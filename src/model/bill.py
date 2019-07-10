from enum import Enum


class ResourceType(Enum):
    ELECTRICITY = 0,
    GAS = 1,
    WATER = 2,
    INTERNET = 3


class Bill:
    def __init__(self, unit, unit_price, total, date):
        self.unit = unit
        self.unit_price = unit_price
        self.total = total
        self.date = date
