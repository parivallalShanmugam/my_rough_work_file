class User:
    #count = 0
    #def __init__(self,username,password):
        #self.username = username
        #self.password = password 
        #User.count += 1

    def login(self):
        print('logging in....'+ self.username)

    def register(self):
        print('registreing....'+ self.username)  

class Student(User):
    def greetStudent(self):
        print('hi student....')          

class Teacher(User):
    def greetTeacher(self):
        print('hello teacher....')

class Tempfaculty(User):
    def greetTempfaculty(self):
        print('nice to have you here')

class Studentfaculty(Student,Teacher):
    def Studentfaculty(self):
        print('hello M.E Students')        