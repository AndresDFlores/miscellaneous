import numpy as np
import matplotlib.pyplot as plt

r1, a1, b1 = (5,0,1)
r2, a2, b2 = (6,6,0)

m = (a2-a1)/(b1-b2)
c = ((a1**2)+(b1**2)+(r2**2)-((a2**2)+(b2**2)+(r1**2)))/(2*(b1-b2))

A = 1+(m**2)
B = 2*((m*(c-b1))-a1)
C = (a1**2)+((c-b1)**2)-(r1**2)

x1 = ((-1*B)+np.sqrt(B**2-(4*A*C)))/(2*A)
y1 = m*x1+c

x2 = (-B-np.sqrt(B**2-(4*A*C)))/(2*A)
y2 = m*x2+c

print((x1, y1), (x2, y2))

theta = np.arange(0,360)


circ1_x = r1*np.cos(theta)+a1
circ1_y = r1*np.sin(theta)+b1

circ2_x = r2*np.cos(theta)+a2
circ2_y = r2*np.sin(theta)+b2


fig, ax = plt.subplots()
ax.plot(circ1_x, circ1_y, '.', 'b')
ax.plot(circ2_x, circ2_y, '.', 'g')
ax.plot([x1, x2], [y1, y2], marker='.', fillstyle='none', linestyle='none', ms=25, color='r')
plt.show() 