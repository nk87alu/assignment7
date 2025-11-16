import numpy as np
import matplotlib.pyplot as plt

m = 2
k = 3
C = float(input("Enter C (0, 2, 1, or 3): "))

dt = 0.01
t = np.arange(0, 20, dt)
y = np.zeros(len(t))
V = np.zeros(len(t))
y[0] = 2
V[0] = 0

# Euler method
for i in range(len(t) - 1):
    dy_dt = V[i]
    dV_dt = -C * V[i] - (k / m) * y[i]
    
    y[i + 1] = y[i] + dy_dt * dt
    V[i + 1] = V[i] + dV_dt * dt

plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title(f'C = {C}')
plt.show()
