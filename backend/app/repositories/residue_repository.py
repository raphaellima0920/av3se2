from app.models.residue import Residue
from .base_repository import BaseRepository

class ResidueRepository(BaseRepository):
    def __init__(self):
        super().__init__(Residue)

    def add_residue(self, data):
        residue = Residue(
            item=data.get("item"),
            type=data.get("type"),
            capacity=data.get("capacity"),
            current_total=data.get("current_total"),
            user_id=data.get("user_id"),
            company_id=data.get("company_id")
        )

        super().add(residue)

        return residue
    
    def get_residue(self, residue_id):
        return super().get(residue_id)
    
    def get_all_residue(self):
        return super().get_all()
    
    def update_residue(self, residue_id, data):
        residue = super().get(residue_id)

        name = data.get("name")
        item = data.get("item")
        type = data.get("type")
        capacity = data.get("capacity")
        current_total = data.get("current_total")
        user_id = data.get("user_id")
        company_id = data.get("company_id")

        if name:
            residue.name = name
        if item:
            residue.item = item
        if type:
            residue.type = type
        if capacity:
            residue.capacity = capacity
        if current_total:
            residue.current_total = current_total
        if user_id:
            residue.user_id = user_id
        if company_id:
            residue.company_id = company_id

        super().update(residue)

        return residue
    
    def delete_residue(self, residue_id):
        residue = super().get(residue_id)
        super().delete(residue)

        return residue