#global variable
users = [
    {
        "id" : 1,
        "username" : "james",
        "email" : "james@gmail.com", #James123
        "password" : "pbkdf2:sha256:50000$5np7XCEk$0bbda50e8a63b77261566f314c8a1f1186be50db81bf2a2b236ea90a82f65c29"
    },
    {
        "id" : 2, #mee123
        "username" : "mee",
        "email" : "me@gmail.com",
        "password" : "pbkdf2:sha256:50000$LZJCWWYO$38fff566776fe47851b1f589ca051877dad52edddd9b7d3853e964b2e07678d0"
    },
    {
        "id" : 3, #mee123
        "username" : "lucy",
        "email" : "lucy@gmail.com",
        "password" : "pbkdf2:sha256:50000$LZJCWWYO$38fff566776fe47851b1f589ca051877dad52edddd9b7d3853e964b2e07678d0"
    }
]

class User(object):    
    '''This class initializes User Model and Stores User Credential'''
    
    def __init__(self, email=None, username=None, password=None):
        self.user_id = len(users)+1
        self.email = email
        self.username = username
        self.password_hash = password

    def add_user(self):
        user = {
            "userid": self.user_id,
            "email": self.email,
            "username": self.username,
            "password":self.password_hash
        }
        users.append(user)
        return users

    def find_user(self,email):
        for user in users:
            if user['email'] == email:
                return user
