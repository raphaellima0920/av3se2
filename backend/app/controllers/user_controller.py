from flask import jsonify, request
from app.repositories.user_repository import UserRepository

class UserController:
    def __init__(self):
        self.user_repository = UserRepository()
    
    def create_user(self):
        data = request.get_json()

        user = self.user_repository.add_user(data)

        return jsonify({
            "message": "Usuário criado com sucesso!",
            "user": user.to_dict()
        }), 201
    
    def get_user(self, user_id):
        user = self.user_repository.get_user(user_id)

        return jsonify({
            "message": "Usuário encontrado com sucesso!",
            "user": user.to_dict()
        }), 201
    
    def get_all_user(self):
        users = self.user_repository.get_all_user()

        return jsonify({
            "message": "Usuários encontrados com sucesso!",
            "users": [user.to_dict() for user in users]
        }), 201
    
    def update_user(self, user_id):
        data = request.get_json()
        user = self.user_repository.update_user(user_id, data)

        return jsonify({
            "message": "Usuário atualizado com sucesso!",
            "user": user.to_dict()
        }), 201
    
    def delete_user(self, user_id):
        user = self.user_repository.delete_user(user_id)

        return jsonify({
            "message": "Usuário deletado com sucesso!",
            "user": user.to_dict()
        }), 201
