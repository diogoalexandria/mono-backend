import jwt
from fastapi import HTTPException, security
from fastapi import HTTPAuthorizationCredentials, HTTPBearer
from passlib import CryptContext
from datetime import datetime, timedelta

class AuthHandler():
    security = HTTPBearer()
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = os.environ['SECRET']

    def hash_password(self, password):
        return self.password_context.hash(password)
    
    def verify_password(self, plain_password, hashed_password):
        return self.password_context.verify(plain_password, hashed_password)
    
    def encode_token(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': 
        }
    

Auth = AuthHandler()