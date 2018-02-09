import random

class MastermindGame(object):
    
    def __init__(self):
        pass

    def generate_comp_code(self):
        computer_code = []
        for n in range(4):
            computer_code.append(random.randint(0, 8))
        return computer_code 

    def get_user_guess(self):
        guess = []
        for n in range(4):
            user_in = guess.append(int(input("Please enter your 4 digit guess (1 digit at a time, press ENTER): "))) 
        return guess

    def evaluate_code(self, guess, code):
        result = ""
        for i in range(4):
            if guess[i] == code[i]:
                result += "B"
                guess[i] = 100
                code[i] = 101
            elif guess[i] in code: 
                result += "W"
        return result

    def main(self):
        code = self.generate_comp_code()
        guess = self.get_user_guess()
        self.evaluate_code(code, guess)


        


         

