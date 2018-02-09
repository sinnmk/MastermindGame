import unittest
from app.mastermind_game import MastermindGame

class TestMastermindGame(unittest.TestCase):

    def setUp(self):
        self.game = MastermindGame()

    def test_can_generate_code(self):
        code = self.game.generate_comp_code()
        self.assertEqual(len(code), 4)

    def test_can_win(self):
        win = self.game.evaluate_code([1, 1, 1, 1], [1, 1, 1, 1] )
        self.assertEqual(win, "BBBB")

    def test_nothing_correct(self):
        nothing = self.game.evaluate_code([1, 2, 3, 4], [5, 6, 7, 8])
        self.assertEqual(nothing, "")

    def test_for_one_correct_position(self):
        one_correct = self.game.evaluate_code([1, 2, 3, 4], [5, 5, 5, 4])
        self.assertEqual(one_correct, "B")

    def test_for_one_misplaced_position(self):
        one_misplaced = self.game.evaluate_code([1, 1, 1, 2], [3, 3, 2, 3])
        self.assertEqual(one_misplaced, "W")

    def test_for_2_correct_and_2_misplaced(self):
        two_two = self.game.evaluate_code([1, 2, 3, 2], [1, 2, 2, 3])
        self.assertEqual(two_two, "BBWW")

    def test_for_one_correct_one_misplaced(self):
        one_one = self.game.evaluate_code([1, 2, 3, 2], [1, 3, 4, 4])
        self.assertEqual(one_one, "BW")

    def test_all_misplaced(self):
        all_misplaced = self.game.evaluate_code([1, 3, 2, 4], [2, 1, 4, 3])
        self.assertEqual(all_misplaced, "WWWW")

    def test_3_misplaced(self):
        three_misplaced = self.game.evaluate_code([3, 2, 1, 4], [2, 3, 4, 2])
        self.assertEqual(three_misplaced, "WWW")

    def test_3_correct(self):
        three_correct = self.game.evaluate_code([1, 2, 3, 4], [2, 2, 3, 4])
        self.assertEqual(three_correct, "BBB")

    def test_1_correct_2_misplaced(self):
        one_two = self.game.evaluate_code([8, 7, 6, 4], [7, 8, 3, 4])
        self.assertEqual(one_two, "WWB")

    def test_2_correct_1_misplaced(self):
        two_one = self.game.evaluate_code([6, 7, 1, 2], [6, 7, 2, 3])
        self.assertEqual(two_one, "BBW")

    def test_can_get_user_guess(self):
        guess = self.game.get_user_guess()
        self.assertEqual(len(guess), 4)


    
        

        

    

    



    

    

    
        
