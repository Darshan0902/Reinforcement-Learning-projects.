import random

class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.num_attempts = 0

    def reset(self):
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.num_attempts = 0

    def guess(self, number):
        self.num_attempts += 1
        if number < self.secret_number:
            return "higher"
        elif number > self.secret_number:
            return "lower"
        else:
            return "correct"

def random_guess_agent(game):
    return random.randint(game.min_num, game.max_num)

def play_game(player1, player2):
    game = NumberGuessingGame()
    game_over = False
    while not game_over:
        guess = player1(game)
        result = game.guess(guess)
        print(f"Player 1 guesses: {guess}")
        print(f"Result: {result}")
        if result == "correct":
            print(f"Player 1 wins in {game.num_attempts} attempts!")
            break
        opponent_guess = player2(game)
        result = game.guess(opponent_guess)
        print(f"Opponent guesses: {opponent_guess}")
        print(f"Result: {result}")
        if result == "correct":
            print(f"Opponent wins in {game.num_attempts} attempts!")
            break

if __name__ == "__main__":
    play_game(random_guess_agent, random_guess_agent)
