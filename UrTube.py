from User import User

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        
    def register (self, nickname, password, age):
        
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return 
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошёл в систему")
                
        
