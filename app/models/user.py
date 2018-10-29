class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
    """ Save the created user to a list of users"""
    def save_users(self,user):
        USERS.append(user)

USERS = []
""" View a list of users"""
def get_users():
    return USERS

@staticmethod
def search_user(username):
    for user in USERS:
        for key in user:
            if user[key] == username:
                return user
            else:
                return username + ' was not found'
