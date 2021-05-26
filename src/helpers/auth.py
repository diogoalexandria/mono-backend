import os
import jwt
from typing import Union, Any
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthHandler():
    security = HTTPBearer()
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = os.environ['SECRET']

    def hash_password(self, password: str):
        return self.password_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str):
        return self.password_context.verify(plain_password, hashed_password)
    
    def encode_token(self, subject: Union[str, Any] , expires_delta: timedelta = None):
        if expires_delta:
            time_expiration = datetime.utcnow() + expires_delta
        else:
            time_expiration = datetime.utcnow() + timedelta(days=0, minutes=30)

        payload = {
            'exp': time_expiration,
            'iat': datetime.utcnow(),
            'sub': subject
        }
        
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )
    
    def decode_token(self, token):
        try:            
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Assinatura do token expirada.')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Token inválido.')
    
    def wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):        
        return self.decode_token(auth.credentials)    

Auth = AuthHandler()