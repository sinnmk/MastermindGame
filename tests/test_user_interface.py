import unittest
from app.user_interface import UserInterface 
from app.mastermind_game import MastermindGame

class TestUserInterface(unittest.TestCase):

    def setUp(self):
        self.console = UserInterface()
        self.game = MastermindGame()

    def test_can_print_hello(self):
        hello = self.console.user_prompt()
        self.assertEqual(hello, "Hello, Welcome to the game MASTERMIND")

    def test_can_display_menu(self):
        menu = self.console.menu_prompt()
        self.assertEqual(menu, "\n(1): Play Game \n(2): Display Rules \n(3): Quit")

    def test_can_display_rules(self):
        rules = self.console.display_rules()
        self.assertEqual(rules, "The objective of this game is to guess a 4 digit code. For every digit that is in the correct place you will receive a black peg. For every digit that you have correct, but in the wrong position, you receive a white peg. For every digit you have wrong, you receive no pegs. You have 10 guesses to crack the code.")

    def test_can_get_user_choice_one(self):
        user_in = self.console.get_user_choice(1)
        self.assertEqual(user_in, self.console.play_game())

    def test_can_get_user_choice_two(self):
        user_in = self.console.get_user_choice(2)
        self.assertEqual(user_in, self.console.display_rules())

    def test_can_get_user_choice_three(self):
        user_in = self.console.get_user_choice(3)
        self.assertEqual(user_in, self.console.leave_game())

        

    
     

    



    
        
    

    

    



    




    



    




