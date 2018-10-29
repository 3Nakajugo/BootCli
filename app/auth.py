from user import User


# Helper functions
def user_signup(username):
    if username:
        role = input('Please provide a valid role: ')
    else:
        print('You must provide a username')
        return
    # check if the user has provided a role
    # if true then prompt the user for a password
    if role:
        password = input('Please provide a password: ')
    # else still prompt the user for a valid role
    else:
        print('You must provide a valid role')
        return
    # if password is provided, use the provided credentials
    # to login by calling the add_account method on the user class to
    # create a new user account
    if password:
        user = User(username=username, role=role, password=password)
        user.save_users(user)

        print(username + ' has successfully signed up')
    # else still prompt the user for a password
    else:
        print('You must provide a password')
        return


def user_login(username):
    if username:
        password = input('Please provide a password: ')
    # else still prompt the user for the username
    else:
        print('You must provide a username!')
        return

    if password:
        # if password is provided, use the provided credentials
        # to login by calling the login method on the user class
        # to login the user
        response = User.search_user(username)
        if isinstance(response, User):
            print(username + ' has successfully logged in')
        # else if the we get a key error then use the provided
        # return a message to the user
        else:
            print(response)
        # else if no password is provided then prompt the user for a password
    else:
        print('You must provide a password')
        return


def user_signup_and_login():
    # get the username from the user
    username = input('Please provide a username: ')
    # check if the user has provided a name
    # if true then prompt the user for an email address
    user_signup(username)
    # if the user has been successfully created, then ask the
    # user user if he would like to login into his new account
    print('Do you want to login into your new account?')
    login = input('Enter (y/n):')
    # if yes, then call the user_login helper method to login the user
    if login == 'y':
        user_login()
    # if not, thank the user for creating an account and return
    if login == 'n':
        print('Thank you for creating an account')


def user_login():
    # get the username from the user
    username = input('Please provide a username: ')
    # check if the user has provided a name
    # if true then prompt the user for a password
    user_login(username)
