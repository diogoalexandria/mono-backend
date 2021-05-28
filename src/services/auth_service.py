from src.models.users_model import UsersModel
from typing import Union
from uuid import UUID
from fastapi import HTTPException
from src.helpers.auth import Auth
from src.helpers.users import is_active

class AuthService():
    def validate_access(self, user: Union[UsersModel, None], password: str):
        if not user:
            raise HTTPException(status_code=400, detail="Usuário inexistente.")
        if not Auth.verify_password(password, user.password):
            raise HTTPException(status_code=400, detail="Senha incorreta.")
        if not is_active(user):
            raise HTTPException(status_code=400, detail="Usuário desativado.")

    def get_token(self, payload: Union[UUID, str]):
        return Auth.encode_token(payload)

AuthService = AuthService()
