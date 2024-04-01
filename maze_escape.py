
from colorama import Fore, Style
import numpy as np
import random
import time

class QLearningAgent:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, min_exploration_rate=0.01, exploration_decay_rate=0.99):
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.min_exploration_rate = min_exploration_rate
        self.exploration_decay_rate = exploration_decay_rate
        self.q_table = np.zeros((num_states, num_actions))

    def choose_action(self, state):
        if random.uniform(0, 1) < self.exploration_rate:
            return random.randint(0, self.num_actions - 1)
        else:
            return np.argmax(self.q_table[state, :])

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state, :])
        td_target = reward + self.discount_factor * self.q_table[next_state, best_next_action]
        td_error = td_target - self.q_table[state, action]
        self.q_table[state, action] += self.learning_rate * td_error

    def decay_exploration_rate(self):
        self.exploration_rate = max(self.min_exploration_rate, self.exploration_rate * self.exploration_decay_rate)

class MazeEscapeRL:
    def __init__(self, size=5):
        self.size = size
        self.num_states = size * size
        self.num_actions = 4  # up, down, left, right
        self.agent_pos = (0, 0)
        self.goal_pos = (size - 1, size - 1)
        self.trap_pos = [(random.randint(0, size-1), random.randint(0, size-1)) for _ in range(size)]
        self.state = self.encode_state(self.agent_pos)

    def encode_state(self, pos):
        return pos[0] * self.size + pos[1]

    def reset(self):
        self.agent_pos = (0, 0)
        self.state = self.encode_state(self.agent_pos)

    def move_agent(self, action):
        new_pos = self.agent_pos
        if action == 0 and self.agent_pos[0] > 0:
            new_pos = (self.agent_pos[0] - 1, self.agent_pos[1])  # up
        elif action == 1 and self.agent_pos[0] < self.size - 1:
            new_pos = (self.agent_pos[0] + 1, self.agent_pos[1])  # down
        elif action == 2 and self.agent_pos[1] > 0:
            new_pos = (self.agent_pos[0], self.agent_pos[1] - 1)  # left
        elif action == 3 and self.agent_pos[1] < self.size - 1:
            new_pos = (self.agent_pos[0], self.agent_pos[1] + 1)  # right
        if new_pos not in self.trap_pos:
            self.agent_pos = new_pos
        self.state = self.encode_state(self.agent_pos)

    def get_reward(self):
        if self.agent_pos == self.goal_pos:
            return 1  # positive reward for reaching the goal
        elif self.agent_pos in self.trap_pos:
            return -1  # negative reward for hitting a trap
        else:
            return 0  # no reward for other positions

    def is_terminal_state(self):
        return self.agent_pos == self.goal_pos or self.agent_pos in self.trap_pos

    def display(self):
        for i in range(self.size):
            row = ''
            for j in range(self.size):
                if (i, j) == self.agent_pos:
                    row += Fore.GREEN + 'A ' + Style.RESET_ALL
                elif (i, j) == self.goal_pos:
                    row += Fore.BLUE + 'G ' + Style.RESET_ALL
                elif (i, j) in self.trap_pos:
                    row += Fore.RED + 'T ' + Style.RESET_ALL
                else:
                    row += '. '
            print(row)
        print()

def train_rl_agent(num_episodes):
    maze = MazeEscapeRL(size=5)
    agent = QLearningAgent(maze.num_states, maze.num_actions)

    for episode in range(num_episodes):
        maze.reset()
        done = False
        total_reward = 0

        while not done:
            action = agent.choose_action(maze.state)
            prev_state = maze.state
            maze.move_agent(action)
            reward = maze.get_reward()
            total_reward += reward
            done = maze.is_terminal_state()
            agent.update_q_table(prev_state, action, reward, maze.state)

        agent.decay_exploration_rate()
        print(f"Episode {episode + 1}: Total Reward = {total_reward}")

def test_rl_agent():
    maze = MazeEscapeRL(size=5)
    agent = QLearningAgent(maze.num_states, maze.num_actions, exploration_rate=0)
    maze.reset()
    maze.display()

    while not maze.is_terminal_state():
        action = agent.choose_action(maze.state)
        maze.move_agent(action)
        maze.display()
        time.sleep(1)

    print("Game Over!")

if __name__ == "__main__":
    train_rl_agent(num_episodes=1000)
    test_rl_agent()
