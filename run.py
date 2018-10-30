import sys

class Menu:
    '''display'''
    def __init__(self):
        self.choices = {
            "1": self.add_account,
            "2": self.user_login,
            "3": self.quit
        }

    def display_menu(self):
        print('''
        User Menu:
        1. Add Account
        2. Login
        3. Quit
        ''')

    def run(self):
        '''Display the menu and respond to 
           user input choices, 
        '''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def add_account(self):
        username = input("Enter username: ")
            

    def user_login(self):
        username = input("Enter username: ")
    
    def show_cnadidate_menu(self):
        print('''
            User Menu:
            1. View Scores
            2. Quit
            ''')
        print("")
        choice = input("choose option: ")
        if choice == 1:
            print("view scores")
        elif choice == 2:
            self.quit()     
        else:
            print("{0} is not a valid choice".format(choice))     

    def show_lfa_menu(self):
        print('''
            User Menu:
            1. Enter Scores
            2. View Scores
            3. Quit
            ''')
        print("")
        choice = input("choose option: ")
        if choice == 1:
            print("enter scores")
        elif choice == 2:
            print("view scores")
        elif choice == 3:
            self.quit()     
        else:
            print("{0} is not a valid choice".format(choice))

    def show_lf_menu(self):
        print('''
            User Menu:
            1. View Scores
            2. Quit
            ''')
        print("")
        choice = input("choose option: ")
        if choice == 1:
            print("view scores")
        elif choice == 2:
            self.quit()     
        else:
            print("{0} is not a valid choice".format(choice))                        




    def add_scores(self):
        print("enter scores")

    def show_scores(self):
        print("view scores")

    def quit(self):
        '''exits the system'''
        print("Thank you for using the system today")
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()