from flask import jsonify, request
from app.repositories.residue_repository import ResidueRepository

class ResidueController:
    def __init__(self):
        self.residue_repository = ResidueRepository()
    
    def create_residue(self):
        data = request.get_json()

        residue = self.residue_repository.add_residue(data)
        
        return jsonify({
            "message": "Residuo criado com sucesso!",
            "residue": residue.to_dict()
        }),201
    
    def get_residue(self, residue_id):
        residue = self.residue_repository.get_residue(residue_id)
        
        return jsonify({
            "message": "Residuo encontrado com sucesso!",
            "residue": residue.to_dict()
        })

    def get_all_residue(self):
        residues = self.residue_repository.get_all_residue()
        
        return jsonify({
            "message": "Residuos encontrados com sucesso!",
            "residues": [residue.to_dict() for residue in residues]
        })
    
    def update_residue(self, residue_id):   
        data = request.get_json()
        residue = self.residue_repository.update_residue(residue_id, data)
        
        return jsonify({
            "message": "Residuo atualizado com sucesso!",
            "residue": residue.to_dict()
        })
    
    def delete_residue(self, residue_id):
        residue = self.residue_repository.delete_residue(residue_id)
        
        return jsonify({
            "message": "Residuo deletado com sucesso!",
            "residue": residue.to_dict()
        })
    