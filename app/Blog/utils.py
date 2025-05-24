from passlib.context import CryptContext


pwd_contxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():

    def hashing_passwod(pwd: str):
        return pwd_contxt.hash(pwd)
    
    def verify_password(plain_password, hashed_password):
        return pwd_contxt.verify(plain_password, hashed_password)

    