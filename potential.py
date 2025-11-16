import numpy as np
import matplotlib.pyplot as plt
from createdgrid import qgrid

e_o = 8.854e-12

data = qgrid(50)
charges = data['charges']
coords = np.array(data['coordinates'])

dx = 0.01
x = np.arange(-10, 10, dx)
y = np.arange(-20, 20, dx)
X, Y = np.meshgrid(x, y)

V = np.zeros_like(X)
for i in range(len(charges)):
    xq, yq = coords[i]
    r = np.sqrt((X - xq)**2 + (Y - yq)**2)
    r = np.where(r < 0.01, 0.01, r)
    V += charges[i] / (4 * np.pi * e_o * r)

V_clipped = np.clip(V, np.percentile(V, 5), np.percentile(V, 95))

Ey, Ex = np.gradient(-V, dx)

plt.figure(figsize=(10, 8))
plt.contourf(X, Y, V_clipped, levels=100, cmap="bwr")
plt.colorbar(label='Potential (V)')

skip = 15
Xnew = X[::skip, ::skip]
Ynew = Y[::skip, ::skip]
ExNew = Ex[::skip, ::skip]
EyNew = Ey[::skip, ::skip]
plt.streamplot(Xnew, Ynew, ExNew, EyNew, color='black', density=1.5, linewidth=0.5)

for i in range(len(charges)):
    color = 'red' if charges[i] > 0 else 'blue'
    plt.plot(coords[i, 0], coords[i, 1], 'o', color=color, markersize=5, markeredgecolor='white', markeredgewidth=0.8)

plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Electric Potential and Field from 50 Random Charges')
plt.show()
