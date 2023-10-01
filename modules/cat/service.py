from typing import Union

from .model import CatModel

class CatService:
    def __init__(self):
        self.cat_model = CatModel()

    def find(self, cat_name: Union[str,None]):

        cats = self.cat_model.find(cat_name)

        if not cats:
            return {"data": [], "message": "Cats is not found"}, 404
        
        return {"data": cats, "message": "OK"}, 200

    
    def create(self, name:str):
        cats = self.cat_model.find()
        cat_id = int(cats[-1].get("id")) + 1

        cat_id = str(cat_id)

        a_new_cat = {
            "id": str(cat_id),
            "name": name,
        }
        self.cat_model.add(a_new_cat)
    
    def get(self, cat_id:str):
        cat = self.cat_model.get(cat_id)

        if not cat:
            return {"data": None, "message": "Cat is not found"}, 404
        
        return {"data": cat, "message": "OK"}, 200