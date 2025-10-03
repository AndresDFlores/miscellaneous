import numpy as np


def rotate_point_2d(point:tuple, theta=0):

    #  rotate a point in 2D space using rotation matrices
    #  point is a tuple with two numeric values, (x, y)
    #  theta is a numeric value in degrees over which the point is rotating


    #  create coordinate matrix
    coord = np.array(
        [
            [point[0]],
            [point[-1]]
        ]
    )


    #  convert degrees to radians
    theta_rad = np.deg2rad(theta)


    #  rotation matrix
    rotation_matrix = np.array(
        [
            [np.cos(theta_rad), -1*np.sin(theta_rad)],
            [np.sin(theta_rad), np.cos(theta_rad)]
        ]
    )


    #  calculate rotated point
    rotated = rotation_matrix@coord


    #  format as tuple for output
    return (*rotated[0], *rotated[-1])



def rotate_point_3d(point:tuple, alpha=0, beta=0, gamma=0, rotation_order:str='xyz'):

    #  rotate a point in 3D space using rotation matrices
    
    #  point is a tuple with two numeric values, (x, y, z)
    #  alpha, beta, gamma are numeric values in degrees over which the point is rotating, Euler angles
    #  rotation_order is a string of three characters indicating the order of rotations (no double axis rotations allowed)

    #  rotating about x-axis: alpha is a numeric value in degrees over which the point is rotating
    #  rotating about y-axis: beta is a numeric value in degrees over which the point is rotating
    #  rotating about z-axis: gamma is a numeric value in degrees over which the point is rotating


    #  create coordinate matrix
    coord = np.array(
        [
            [point[0]],
            [point[1]],
            [point[2]]
        ]
    )


    #  convert degrees to radians
    alpha_rad = np.deg2rad(alpha)  #  x-axis rotation matrix - Roll
    beta_rad = np.deg2rad(beta)  #  y-axis rotation matrix - Pitch
    gamma_rad = np.deg2rad(gamma)  #  z-axis rotation matrix - Yaw


    rotation_matrices = dict(

        x=[
            [1, 0, 0],
            [0, np.cos(alpha_rad), -1*np.sin(alpha_rad)],
            [0, np.sin(alpha_rad), np.cos(alpha_rad)]
        ],

        y=[
            [np.cos(beta_rad), 0, np.sin(beta_rad)],
            [0, 1, 0],
            [-1*np.sin(beta_rad), 0, np.cos(beta_rad)]
        ],

        z=[
            [np.cos(gamma_rad), -1*np.sin(gamma_rad), 0],
            [np.sin(gamma_rad), np.cos(gamma_rad), 0],
            [0, 0, 1]
        ]

    )

    #  build rotation matrix based on indicated rotation order
    rotation_matrix = np.array(rotation_matrices[rotation_order[0]])
    for axis in rotation_order[1:]:
        rotation_matrix@=np.array(rotation_matrices[axis])


    #  calculated rotated point
    rotated = rotation_matrix@coord


    #  format as tuple for output
    return (*rotated[0], *rotated[1], *rotated[2])



if __name__=="__main__":

    #  perform the same point identically using 2D and 3D rotation matrices

    rotated_point_2d = rotate_point_2d(point=(0,1), theta=90)
    print(rotated_point_2d)

    rotated_point_2d = rotate_point_2d(point=rotated_point_2d, theta=-90)
    print(rotated_point_2d)

    print('---')

    rotated_point_3d = rotate_point_3d(point=(0,1,0), alpha=0, beta=0, gamma=90, rotation_order='z')
    print(rotated_point_3d)

    rotated_point_3d = rotate_point_3d(point=rotated_point_3d, alpha=0, beta=0, gamma=-90, rotation_order='z')
    print(rotated_point_3d)
