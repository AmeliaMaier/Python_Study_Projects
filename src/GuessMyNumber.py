import random


class ContentLake:

    def __init__(self):
        pass

    def get_random_number(self):
        return random.randint(1, 51)


    def print_past_guesses(self, past_guesses, past_notes):
        if len(past_guesses) > 0:
            print(f"Past guesses: ")
            for guess in past_guesses:
                print(f"{guess}: {past_notes[guess]}")

    def check_guess(self, current_guess, correct_answer, last_guess):
        try:
            if current_guess == 'Q':
                return True
            elif int(current_guess) == correct_answer:
                current_note = "That is correct."
                print(current_note)
                return True
            elif abs(int(current_guess) - correct_answer) <= 5:
                current_note = "You're hot. Try again."
            elif not last_guess == -1:
                if abs(int(current_guess) - correct_answer) < abs(int(last_guess) - correct_answer):
                    current_note = "Getting warmer! Try again"
                elif abs(int(current_guess) - correct_answer) > abs(int(last_guess) - correct_answer):
                    current_note = "Getting cooler, try again."
                else:
                    current_note = "That is not correct, try again."
            elif abs(int(current_guess) - correct_answer) > 25:
                current_note = "You're freezing. Try again"
            else:
                current_note = "That is not correct, try again."
            print(current_note)
            return current_note
        except ValueError:
            return False

    def run_game(self):
        try_again = 'Y'
        current_guess = -1
        while try_again == 'Y' and not current_guess == 'Q':
            current_guess = -1
            last_guess = None
            past_guesses = []
            past_notes = dict({})
            current_note = ''
            correct_answer = self.get_random_number()
            while not current_guess == correct_answer:
                last_guess = current_guess
                self.print_past_guesses(past_guesses, past_notes)
                current_guess = input("Guess a number, 1-50. Type Q to quit: ")
                current_note = self.check_guess(current_guess, correct_answer, last_guess)
                if current_note is True:
                    break
                elif current_note is False:
                    print('Please enter a number or the letter Q only.')
                else:
                    past_guesses.append(current_guess)
                    past_notes[current_guess] = current_note
            if not current_guess == 'Q':
                try_again = input("Enter Y to try again: ")


if __name__ == '__main__':
    game = ContentLake()
    game.run_game()
