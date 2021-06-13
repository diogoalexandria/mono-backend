import os
from src.schemas.auth_schemas import TokenTypes
import jwt
from uuid import UUID
from typing import Union, Any
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthHandler():
    security = HTTPBearer()
    password_context = CryptContext( schemes=["bcrypt"], deprecated="auto" )
    secret = os.environ['SECRET']
    refresh_secret = os.environ['REFRESH_SECRET']

    def hash_password( self, password: str ):
        return self.password_context.hash(password)
    
    def verify_password( self, plain_password: str, hashed_password: str ):
        return self.password_context.verify(plain_password, hashed_password)
    
    def encode_token( self, type: TokenTypes, subject: Union[str, Any] , expires_delta: timedelta = None ):

        if expires_delta:
            time_expiration = datetime.utcnow() + expires_delta
        else:
            time_expiration = datetime.utcnow() + timedelta(days=0, minutes=30)        
        
        if isinstance(subject, UUID):                        
            subject = str(subject)

        payload = {            
            'iat': datetime.utcnow(),
            'sub': subject
        }

        if type == 'refresh':
            secret = self.refresh_secret
        else:
            secret = self.secret
            payload['exp'] = time_expiration
        
        return jwt.encode(

            payload,
            secret,
            algorithm ='HS256'

        )        
    
    def decode_token( self, token: str ):
        try:            
            payload = jwt.decode( token, self.secret, algorithms=['HS256'] )
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException( status_code=401, detail='Assinatura do token expirada.' )
        except jwt.InvalidTokenError as e:
            raise HTTPException( status_code=401, detail='Token inválido.' )
    
    def wrapper( self, auth: HTTPAuthorizationCredentials = Security(security) ):        
        return self.decode_token(auth.credentials)    

Auth = AuthHandler()