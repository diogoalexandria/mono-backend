import jwt
from fastapi import HTTPException, Security
from fastapi import HTTPAuthorizationCredentials, HTTPBearer
from passlib import CryptContext
from datetime import datetime, timedelta

class AuthHandler():
    security = HTTPBearer()
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = os.environ['SECRET']

    def hash_password(self, password: str):
        return self.password_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str()):
        return self.password_context.verify(plain_password, hashed_password)
    
    def encode_token(self, subject: Union[str, Any] , expires_delta: timedelta = None):
        if expires_delta:
            time_expiration = datetime.utcnow() + expires_delta
        else:
            time_expiration = datetime.utcnow() + timedelta(days=0, minutes=5)

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
    
    def deccode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithm=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Assinatura do token expirada.')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Token inválido.')
    
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.deccode_token(auth.credentials)

Auth = AuthHandler()