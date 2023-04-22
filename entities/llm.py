from entities.base import BaseEntity


class LLMEntity(BaseEntity):
    def __init__(self, model):
        super().__init__()
        self.model = ""
        self.messages = []
