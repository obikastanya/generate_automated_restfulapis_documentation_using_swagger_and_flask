from abc import ABC

class Schema(ABC):
    def __init__(self):
        self.name : str

    def create_name(self, model_name:str)->str:
        return f"{self.name.lower()}_{model_name.lower()}"