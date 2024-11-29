from flask import jsonify, request
from app.repositories.company_repository import CompanyRepository

class CompanyController:
    def __init__(self):
        self.company_repository = CompanyRepository()

    def create_company(self):
        data = request.get_json()

        name = data.get("name")

        company = self.company_repository.add_company(name)
        
        return jsonify({
            "message": "Pasta criada com sucesso!",
            "company": company.to_dict()
            }), 201
    
    def get_company(self, company_id):
        company = self.company_repository.get_company(company_id)

        return jsonify({
            "message": "Pasta encontrada com sucesso!",
            "company": company.to_dict()
        })
    
    def get_all_company(self):
        companies = self.company_repository.get_all_company()

        return jsonify({
            "message": "Pastas encontradas com sucesso!",
            "companies": [company.to_dict() for company in companies]
        })
    
    def update_company(self, company_id):
        data = request.get_json()
        company = self.company_repository.update_company(company_id, data)

        return jsonify({
            "message": "Pasta atualizada com sucesso!",
            "company": company.to_dict()
        })
    
    def delete_company(self, company_id):
        company = self.company_repository.delete_company(company_id)
        
        return jsonify({
            "message": "Pasta deletada com sucesso!",
            "company": company.to_dict()
        })
    