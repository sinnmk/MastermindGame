from app.mastermind_game import MastermindGame 

class UserInterface(object):

    def __init__(self):
        pass

    def user_prompt(self):
        return ("Hello, Welcome to the game MASTERMIND")

    def menu_prompt(self):
        return ("\n(1): Play Game \n(2): Display Rules \n(3): Quit")

    def play_game(self):
        self.game = MastermindGame()

    def display_rules(self):
        return ("The objective of this game is to guess a 4 digit code. For every digit that is in the correct place you will receive a black peg. For every digit that you have correct, but in the wrong position, you receive a white peg. For every digit you have wrong, you receive no pegs. You have 10 guesses to crack the code.")

    def leave_game(self):
        return

    def get_user_choice(self, choice):
        choice = int(input("\nChoose what you would like to do:  \n"))

        if (choice == 1): 
            self.play_game()
        elif (choice == 2): 
            self.display_rules()
        elif (choice == 3): 
            self.leave_game()
        else: 
            print("You have entered an invalid choice. Please try again!")

    def main(self):
        self.user_prompt()
        self.menu_prompt()
        choice = self.get_user_choice()
        self.get_user_choice(choice)




    




                




