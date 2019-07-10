from src.model.bill import ResourceType


class SmartHome:
    def __init__(self, designer, devices, monthly_internet=0):
        self.monthly_internet = monthly_internet
        self.designer = designer
        self.devices = devices
        self.bills = []

    def all_bills(self):
        if self.bills:
            return self.bills
        # TODO: ако је листа self.bills празна, за претходних шест месеци направити рачуне и убацити их у листу.

    def electricity_bills(self):
        return filter(lambda b: b.unit == ResourceType.ELECTRICITY, self.all_bills())

    def water_bills(self):
        return filter(lambda b: b.unit == ResourceType.WATER, self.all_bills())

    def gas_bills(self):
        return filter(lambda b: b.unit == ResourceType.GAS, self.all_bills())

    def internet_bills(self):
        return filter(lambda b: b.unit == ResourceType.INTERNET, self.all_bills())
