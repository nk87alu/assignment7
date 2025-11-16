import numpy as np
from matplotlib import pyplot as pp

v_initial = 4
h = 0.1
m = 70
P = 400

def myODE(v):
    return P / (m * v)

def eulerStep(v):
    return v + myODE(v) * h

x = np.arange(0, 200 + h, h)
v = [v_initial]

for i in range(len(x) - 1):
    v.append(eulerStep(v[-1]))

pp.plot(x, v)
pp.xlabel('Time (s)')
pp.ylabel('Velocity (m/s)')
pp.title('Cyclist Velocity vs Time')
pp.grid()
#pp.savefig('bicycle.png')
pp.show()
