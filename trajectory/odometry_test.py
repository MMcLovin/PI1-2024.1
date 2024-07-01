import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Dashboard', 'dashboard', 'BANCO_MYSQL')))
from banco_MYSQL import get_velocities, criar_conexao, fechar_conexao
import numpy as np
import matplotlib.pyplot as plt
import random

# global variables
R=67.25/200                # wheel radius
L=(220 - 20.19)/100        # distance between the wheels
n=21                       # number of encoder ticks per wheel revolution, with 192 ticks, the velocity needed to do a 90 degree turn is 236

def generate_xy(v_left, v_right):
    x_pos = [0]
    y_pos = [0]
    theta = 0  # initial heading

    for l, r in zip(v_left, v_right):
        dr = r * ((2 * np.pi * R) / n)  # distance traveled by the right wheel
        dl = l * ((2 * np.pi * R) / n)  # distance traveled by the left wheel
        d = (dr + dl) / 2               # total distance traveled by the middle point between the wheels
        alfa = (dr - dl) / L            # change in heading

        theta += alfa  # update heading
        x = d * np.cos(theta)
        y = d * np.sin(theta)

        # update the position relative to the last position
        x_pos.append(x_pos[-1] + x)
        y_pos.append(y_pos[-1] + y)

    plot_trajectory(x_pos, y_pos)

def plot_trajectory(x_pos, y_pos):
    plt.plot(x_pos, y_pos, marker='o', color='b', label='Trajectory')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Trajectory of Line Follower Robot')
    plt.grid(True)
    plt.show()

def simulate_turns(v_left, v_right):
    for i in range(len(v_left)):
        turn = random.randint(0, 1)
        # turn left
        if i % 20 == 0 and i != 0:
            v_left[i] = 0
            v_right[i] = 31.2
            #25
def main():
    #con = criar_conexao("localhost", "root", "", "ProjetoPI1")

    #data = get_velocities(con)
    #v_left = data[0]
    #v_right = data[1]

    # when both velocities are the same, the robot moves in a straight line
    v_left = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    v_right = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    # duh
    simulate_turns(v_left, v_right)

    generate_xy(v_left, v_right)

    #fechar_conexao(con)

main()
