from entities.base import BaseEntity


class EmployeeEntity(BaseEntity):
    def __init__(self, name, roles):
        super().__init__()
        self.name = name
        self.mini_bio = ""
        self.experiences = []
        self.roles = roles
