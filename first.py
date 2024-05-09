class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password 

    def login(self):
        print('logging in....'+ self.username)

    def register(self):
        print('registreing....'+ self.username)    

