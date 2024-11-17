import bcrypt

class User:
    
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_passwod(password)
        self.age = age
        
    def hash_passwod(self, password):
        # Генерация соли
        salt = bcrypt.gensalt()
        # Хэширование и соление пароля 
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password