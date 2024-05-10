import numpy as np
import matplotlib.pyplot as plt
import random as rng

# Parameters
wheelbase = 0.1         # Wheelbase of the robot (distance between the wheels)
turn_radius = 0.15      # Radius of the turn
speed = 1               # Robot simulated speed

# Simulation time
dt = 0.01
timesteps = 100
time = np.arange(0, timesteps * dt, dt)

# Simulate turn
trajectory_x = []
trajectory_y = []
theta = 0               # Initial orientation of the robot

# generating mock x and y coordinates for the robot
# this will be replaced by the data collected from the sensors and stored in the database
for t in time:
    # Update robot position
    x = turn_radius * np.sin(speed * t / turn_radius)
    y = turn_radius - turn_radius * np.cos(speed * t / turn_radius)
    
    # Update robot orientation
    theta = (speed / turn_radius)

    theta = (speed / turn_radius) 
    
    trajectory_x.append(x)
    trajectory_y.append(y)

# Plot trajectory as XY dots
plt.plot(trajectory_x, trajectory_y, 'b', markersize=2)  # Plot XY dots
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simulated Turn of the Line Follower Robot')
plt.grid(False)
plt.axis('on')

# Set the spines positions to be in the middle
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()


