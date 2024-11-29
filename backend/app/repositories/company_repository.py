from app.models.company import Company
from .base_repository import BaseRepository

class CompanyRepository(BaseRepository):
    def __init__(self):
        super().__init__(Company)

    def add_company(self, name):
        company = Company(name=name)
        super().add(company)

        return company
    
    def get_company(self, company_id):
        return super().get(company_id)
    
    def get_all_company(self):
        return super().get_all()
    
    def update_company(self, company_id, data):
        company = super().get(company_id)
        company.name = data.get("name")
        
        super().update(company)

        return company
    
    def delete_company(self, company_id):
        company = super().get(company_id)
        super().delete(company)

        return company 
    
