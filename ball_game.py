import numpy as np
import matplotlib.pyplot as plt

class GridWorld:
    def __init__(self, size=5):
        self.size = size
        self.grid = np.zeros((size, size))
        self.start_pos = (0, 0)
        self.goal_pos = (size-1, size-1)
        self.cur_pos = self.start_pos
        self.actions = ['up', 'down', 'left', 'right']
        self.num_actions = len(self.actions)
        self.reward = 0
        self.done = False

    def reset(self):
        self.cur_pos = self.start_pos
        self.reward = 0
        self.done = False
        return self.cur_pos

    def step(self, action):
        if action == 'up':
            new_pos = (self.cur_pos[0] - 1, self.cur_pos[1])
        elif action == 'down':
            new_pos = (self.cur_pos[0] + 1, self.cur_pos[1])
        elif action == 'left':
            new_pos = (self.cur_pos[0], self.cur_pos[1] - 1)
        elif action == 'right':
            new_pos = (self.cur_pos[0], self.cur_pos[1] + 1)

        if 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size:
            self.cur_pos = new_pos

        if self.cur_pos == self.goal_pos:
            self.reward = 1
            self.done = True
        else:
            self.reward = 0

        return self.cur_pos, self.reward, self.done

def random_policy():
    return np.random.choice(['up', 'down', 'left', 'right'])

def visualize(grid_world, episodes=10):
    for _ in range(episodes):
        state = grid_world.reset()
        plt.imshow(grid_world.grid, cmap='gray', origin='lower')
        plt.scatter(state[1], state[0], color='red', marker='o', s=100)
        plt.title("Grid World")
        plt.axis('off')
        plt.show()
        done = False
        while not done:
            action = random_policy()
            next_state, reward, done = grid_world.step(action)
            plt.imshow(grid_world.grid, cmap='gray', origin='lower')
            plt.scatter(next_state[1], next_state[0], color='red', marker='o', s=100)
            plt.title("Grid World")
            plt.axis('off')
            plt.show()
            if done:
                print("Goal reached!")
                break

if __name__ == "__main__":
    grid_world = GridWorld()
    visualize(grid_world)
