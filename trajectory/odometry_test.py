import sys
import os
#sys.path.append("../")  # Corrected path if necessary
#print(sys.path)
#from Dashboard.dashboard.BANCO_MYSQL import banco_MYSQL
# Add the path to the Dashboard module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Dashboard', 'dashboard', 'BANCO_MYSQL')))
from banco_MYSQL import get_velocities, criar_conexao, fechar_conexao
import numpy as np
import matplotlib.pyplot as plt

# global variables
R=3.25      # wheel radius
L=16        # distance between the wheels
n=192       # number of encoder ticks per wheel revolution

def generate_xy(v_left, v_right):
    x_pos = [0]
    y_pos = [0]
    theta = 0  # initial heading

    for l, r in zip(v_left, v_right):
        dr = r * ((2 * np.pi * R) / n)  # distance traveled by the right wheel
        dl = l * ((2 * np.pi * R) / n)  # distance traveled by the left wheel
        d = (dr + dl) / 2               # total distance traveled
        alfa = (dr - dl) / L            # change in heading

        theta += alfa  # update heading
        x = d * np.cos(theta)
        y = d * np.sin(theta)

        # update the position relative to the last position
        x_pos.append(x_pos[-1] + x)
        y_pos.append(y_pos[-1] + y)

    plot_trajectory(x_pos, y_pos)

def plot_trajectory(x_pos, y_pos):
    plt.plot(x_pos, y_pos)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Trajectory of Line Follower Robot')
    plt.grid(True)
    plt.show()

def main():
    con = criar_conexao("localhost", "root", "", "ProjetoPI1")

    data = get_velocities(con)
    v_left = data[0]
    v_right = data[1]
    v_left =  [0.2, 0.14, 0.74, 0.0 , 0.21, 0.34, 0.92, 0.0, 0.05, 0.49, 0.74, 0.27, 0.78, 0.32, 0.21, 0.75, 0.38, 0.71, 0.77, 0.8]
    v_right = [0.2, 0.14, 0.74, 0.52, 0.21, 0.34, 0.92, 0.9, 0.05, 0.49, 0.74, 0.27, 0.78, 0.32, 0.21, 0.75, 0.38, 0.71, 0.77, 0.8]
    
    time = data[2]

    generate_xy(v_left, v_right)

    fechar_conexao(con)

main()
