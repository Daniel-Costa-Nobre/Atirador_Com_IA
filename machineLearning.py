# NOTE FOR BRAZILIAN PEOPLE -------> Por favor leia o código com o nome machineLearningBrazil.md
import numpy as np
import random

# Creating reward list
rewards = [
    [1, 1, 1, 1, 1],    # Bigger place to shoot = fewer points
    [-1, 10, 10, 10, 10],
    [-1, -1, 100, 100, 100],
    [-1, -1, -1, 1000, 1000],
    [-1, -1, -1, -1, 10000]    # Smaller place to shoot = more points
]

# This function randomizes the shooting level
def set_shooting_level():
    return np.random.randint(0, 5)

# The initial shoot for the first experience
first_shoot = set_shooting_level()

# Creating a function that can get a random action (if something is reached the bot get rewards)
def get_action(current_state, reward):
    available_action = []
    for action, reward_value in enumerate(reward[current_state]):
        if reward_value != -1:
            available_action.append(action)
    return random.choice(available_action)

# Creating quality matrix & gamma
matrix_q = np.zeros((5, 5))
gamma = 0.8

def take_action(current_state, reward_matrix, gamma):
    # First, we shoot a random place with the "get_action" function
    new_shoot = get_action(current_state, reward_matrix)
    print("Robot shoot:", new_shoot)

    # Collected the variable, it's time to get a reward from the rewards matrix(based on the x and y axis of the shoot)
    current_reward = reward_matrix[current_state][new_shoot]
    print("New reward! +", current_reward, "points")

    # New value with quality
    max_q_value = np.max(matrix_q[new_shoot])

    # Updating quality matrix with belman equation
    matrix_q[current_state][new_shoot] = current_reward + gamma * 0
    print("Value of the reward stored in 'matrix_q':\n\n", matrix_q)


# TEST!!!
take_action(first_shoot, rewards, gamma)


# Explanation of the code:
# The objective is making a functional shooting bot;
# The bot tries a random level of shooting, it can be easy or hard;
# Based on how hard the bot get the level, he get more points than in a easier level;
# In all levels if the bot misses, he loses 1 point
# This first push is just for starting setting the reward list, the get_action and set_shooting_level function.
