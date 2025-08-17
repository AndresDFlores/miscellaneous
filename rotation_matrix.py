import numpy as np


def rotate_point_2d(point:tuple, angle):
    #  point should be two numeric values, (x, y)
    #  angle should be a numeric value in degrees


    #  create coordinate matrix
    coord = np.array(
        [
            [point[0]],
            [point[-1]]
        ]
    )


    #  convert degrees to radians
    theta_rad = np.deg2rad(angle)


    #  rotation matrix
    rotation_matrix = np.array(
        [
            [np.cos(theta_rad), -1*np.sin(theta_rad)],
            [np.sin(theta_rad), np.cos(theta_rad)]
        ]
    )


    #  calculated rotated point
    rotated = rotation_matrix@coord


    #  format as tuple for output
    return (*rotated[0], *rotated[-1])



if __name__=="__main__":

    rotated_point = rotate_point_2d(point=(0,1), angle=90)
    print(rotated_point)

    rotated_point = rotate_point_2d(point=rotated_point, angle=-90)
    print(rotated_point)