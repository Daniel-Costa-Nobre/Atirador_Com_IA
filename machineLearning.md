import numpy as np
import random

# Lista de recompensas
rewards = [
    [1, 1, 1, 1, 1],    # Um lugar maior para atirar = menos pontos
    [-1, 10, 10, 10, 10],
    [-1, -1, 100, 100, 100],
    [-1, -1, -1, 1000, 1000],
    [-1, -1, -1, -1, 10000]    # Um lugar menor para atirar = mais pontos
]

# Essa função randomiza o nível de tiro
def set_shooting_level():
    return np.random.randint(0, 5)

# O tiro inicial para a primeira experiência
first_shoot = set_shooting_level()

# Criando uma função que pode obter uma ação aleatória (se algo for atingido o robô recebe recompensas)
def get_action(current_state, reward):
    available_action = []
    for action, reward_value in enumerate(reward[current_state]):
        if reward_value != -1:
            available_action.append(action)
    return random.choice(available_action)

# Criando matriz de qualidade & gamma
matrix_q = np.zeros((5, 5))
gamma = 0.8

def take_action(current_state, reward_matrix, gamma):
    # Primeiro, atiramos em um lugar aleatório com a função "get_action"
    new_shoot = get_action(current_state, reward_matrix)
    print("Robot shoot:", new_shoot)

    # Coletada a variável, é hora de obter uma recompensa da matriz de recompensas (com base no eixo x e y do tiro)
    current_reward = reward_matrix[current_state][new_shoot]
    print("Nova recompensa! +", current_reward, "pontos")

    # Novo valor com qualidade
    max_q_value = np.max(matrix_q[new_shoot])

    # Atualizando a matriz de qualidade com a equação de Bellman
    matrix_q[current_state][new_shoot] = current_reward + gamma * 0
    print("Valor da recompensa armazenada em 'matrix_q':\n\n", matrix_q)


# TESTE!!!
take_action(first_shoot, rewards, gamma)


# Explicação do código:
# O objetivo é fazer um bot de tiro funcional;
# O bot tenta um nível aleatório de tiro, que pode ser fácil ou difícil;
# Com base em quão difícil o bot acerta o nível, ele ganha mais pontos do que em um nível mais fácil;
# Em todos os níveis, se o bot errar, ele perde 1 ponto.
# Este primeiro push é apenas para começar a configurar a lista de recompensas, a função get_action e set_shooting_level.
