from typing import Union

cats = [
    {"id": "1", "name": "Whiskers"},
    {"id": "2", "name": "Fluffy"},
    {"id": "3", "name": "Shawn"},
]


class CatModel:
    def find(self, cat_name: Union[str, None]):
        if not cat_name:
            return {"data": cats, "message": "OK"}, 200

        _cats = []
        for cat in cats:
            if cat.get("name").lower() == cat.lower():
                _cats.append(cat)

        if not _cats:
            return {"data": [], "message": "Cats is not found"}, 404

        return {"data": cats, "message": "OK"}, 200

    def add(self, a_new_cat):
        cats.append(a_new_cat)

        return {"data": a_new_cat, "message": "OK"}, 201

    def get(self, cat_id: str):
        for cat in cats:
            if cat.get("id") == cat_id:
                return {"data": cat, "message": "OK"}, 200

        return {"data": {}, "message": "Cat is not found"}, 404
