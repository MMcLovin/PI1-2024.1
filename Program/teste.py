import numpy as np

def calculate_trajectory(rpm_left, rpm_right, R, radius, time_duration, time_step):
    """
    Calcula os pontos x e y do percurso a partir do RPM das rodas.

    :param rpm_left: RPM da roda esquerda
    :param rpm_right: RPM da roda direita
    :param R: Distância entre as rodas (em metros)
    :param radius: Raio das rodas (em metros)
    :param time_duration: Duração total da simulação (em segundos)
    :param time_step: Intervalo de tempo entre cada cálculo (em segundos)
    :return: Listas de pontos x e y
    """
    # Convert RPM to radians per second
    omega_left = (rpm_left * 2 * np.pi) / 60
    omega_right = (rpm_right * 2 * np.pi) / 60

    # Convert angular velocity to linear velocity
    v_left = omega_left * radius
    v_right = omega_right * radius

    # Initialize variables
    x, y, theta = 0, 0, 0
    x_points, y_points = [x], [y]

    for _ in range(int(time_duration / time_step)):
        # Calculate linear and angular velocities
        v = (v_right + v_left) / 2
        omega = (v_right - v_left) / R

        # Update position and orientation
        x += v * np.cos(theta) * time_step
        y += v * np.sin(theta) * time_step
        theta += omega * time_step

        # Store the points
        x_points.append(x)
        y_points.append(y)

    return x_points, y_points

# Parâmetros de exemplo
rpm_left = 60      # RPM da roda esquerda
rpm_right = 120    # RPM da roda direita
R = 0.5            # Distância entre as rodas (em metros)
radius = 0.1       # Raio das rodas (em metros)
time_duration = 1 # Duração da simulação (em segundos)
time_step = 0.1    # Intervalo de tempo entre cada cálculo (em segundos)

# Calcular a trajetória
x_points, y_points = calculate_trajectory(rpm_left, rpm_right, R, radius, time_duration, time_step)

# Plotar a trajetória
import matplotlib.pyplot as plt

plt.plot(x_points, y_points, marker='o')
plt.title("Trajetória do Robô Diferencial")
plt.xlabel("X (metros)")
plt.ylabel("Y (metros)")
plt.grid()
plt.show()
