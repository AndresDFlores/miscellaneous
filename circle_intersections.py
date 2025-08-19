import numpy as np


def get_intersections_alg(circ_1:tuple, circ_2:tuple):
    #  each circ_n tuple should define a circle: (radius, center_x, center_y)

    r1, a1, b1 = circ_1
    r2, a2, b2 = circ_2

    m = (a2-a1)/(b1-b2)
    c = ((a1**2)+(b1**2)+(r2**2)-((a2**2)+(b2**2)+(r1**2)))/(2*(b1-b2))

    A = 1+(m**2)
    B = 2*((m*(c-b1))-a1)
    C = (a1**2)+((c-b1)**2)-(r1**2)

    x1 = ((-1*B)+np.sqrt(B**2-(4*A*C)))/(2*A)
    y1 = m*x1+c

    x2 = (-B-np.sqrt(B**2-(4*A*C)))/(2*A)
    y2 = m*x2+c

    return (x1, y1), (x2, y2)



def get_intersections_linalg(circ_1:tuple, circ_2:tuple, circ_3:tuple):
    #  each circ_n tuple should define a circle: (radius, center_x, center_y)

    r1, x1, y1 = circ_1
    r2, x2, y2 = circ_2
    r3, x3, y3 = circ_3

    A = 2*(x2-x1)
    B = 2*(y2-y1)
    C = r1**2-r2**2-x1**2+x2**2-y1**2+y2**2

    D = 2*(x3-x2)
    E = 2*(y3-y2)
    F = r2**2-r3**2-x2**2+x3**2-y2**2+y3**2

    return np.linalg.inv([[A, B], [D, E]])@[[C], [F]]



if __name__=="__main__":

    import matplotlib.pyplot as plt


    #  circle definitions
    r1, a1, b1 = (3.16, 7, 1)
    r2, a2, b2 = (9.43, 13, 12)
    r3, a3, b3 = (10.63, 1, 12)


    #  define domain in degrees
    theta = np.arange(0,360,.01)


    #  circle 1 points
    circ1_x = r1*np.cos(theta)+a1
    circ1_y = r1*np.sin(theta)+b1


    #  circle 2 points
    circ2_x = r2*np.cos(theta)+a2
    circ2_y = r2*np.sin(theta)+b2


    #  circle 3 points
    circ3_x = r3*np.cos(theta)+a3
    circ3_y = r3*np.sin(theta)+b3


    #  three-circle intersection linear algebra

    intersection = get_intersections_linalg(
        circ_1=(r1,a1,b1), 
        circ_2=(r2,a2,b2),
        circ_3=(r3,a3,b3),
    )

    print(intersection)

    fig, ax = plt.subplots()
    ax.plot(circ1_x, circ1_y, '.', 'b', ms=1)
    ax.plot(circ2_x, circ2_y, '.', 'g', ms=1)
    ax.plot(circ3_x, circ3_y, '.', 'o', ms=1)
    ax.plot(intersection[0], intersection[-1], marker='.', fillstyle='none', linestyle='none', ms=25, color='r')
    ax.set_aspect('equal', adjustable='box')
    plt.show()


    #  two-circle intersection algebraic

    intersection_1, intersection_2 = get_intersections_alg(
        circ_1=(r1,a1,b1), 
        circ_2=(r2,a2,b2)
    )

    print(
        intersection_1,
        intersection_2
    )


    fig, ax = plt.subplots()
    ax.plot(circ1_x, circ1_y, '.', 'b', ms=1)
    ax.plot(circ2_x, circ2_y, '.', 'g', ms=1)
    ax.plot([intersection_1[0], intersection_2[0]], [intersection_1[-1], intersection_2[-1]], marker='.', fillstyle='none', linestyle='none', ms=25, color='r')
    ax.set_aspect('equal', adjustable='box')
    plt.show()