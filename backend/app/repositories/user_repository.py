from app.models.user import User
from .base_repository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def add_user(self, data):
        user = User(
            name=data.get("name"),
            email=data.get("email"),
            password=data.get("password"),
            company_id=data.get("company_id")
        )
        super().add(user)

        return user
    
    def get_user(self, user_id):
        return super().get(user_id)
    
    def get_all_user(self):
        return super().get_all()
    
    def update_user(self, user_id, data):
        user = super().get(user_id)

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password
        
        super().update(user)

        return user
    
    def delete_user(self, user_id):
        user = super().get(user_id)
        super().delete(user)

        return user
    