import numpy as np
import random
import matplotlib.pyplot as plt

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))  # 3x3 game board
        self.current_player = 1  # Player 1 starts
        self.game_over = False
        self.winner = None

    def reset(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1
        self.game_over = False
        self.winner = None
        return self.board

    def get_available_moves(self):
        return np.argwhere(self.board == 0)

    def make_move(self, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = self.current_player
            if self.check_winner():
                self.game_over = True
                self.winner = self.current_player
            elif len(self.get_available_moves()) == 0:
                self.game_over = True
            else:
                self.current_player = -self.current_player
            return True
        else:
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals for winning condition
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] != 0:
                return True
            if self.board[0, i] == self.board[1, i] == self.board[2, i] != 0:
                return True
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2] != 0:
            return True
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0] != 0:
            return True
        return False

def random_agent(board):
    available_moves = np.argwhere(board == 0)
    return random.choice(available_moves)

def visualize_game(game):
    symbols = {-1: 'X', 0: ' ', 1: 'O'}
    fig, ax = plt.subplots()
    ax.matshow(game.board, cmap='Pastel1')
    for i in range(3):
        for j in range(3):
            ax.text(j, i, symbols[game.board[i, j]], va='center', ha='center', fontsize=40, color='black')
    plt.title("Tic-Tac-Toe")
    plt.axis('off')
    plt.show()

def play_game(agent1, agent2, visualize=True):
    game = TicTacToe()
    while not game.game_over:
        if game.current_player == 1:
            row, col = agent1(game.board)
        else:
            row, col = agent2(game.board)
        game.make_move(row, col)
        if visualize:
            visualize_game(game)
    if game.winner is None:
        print("It's a draw!")
    else:
        print(f"Player {game.winner} wins!")

if __name__ == "__main__":
    play_game(random_agent, random_agent)
