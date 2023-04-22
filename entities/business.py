from entities.base import BaseEntity


class BusinessEntity(BaseEntity):
    def __init__(self):
        super().__init__()
        self.foundation_date = None
        self.keywords = []
        self.name = ""
        self.employees = 0
        self.revenue = 0
        self.products = []
        self.services = []
        self.employees = []
