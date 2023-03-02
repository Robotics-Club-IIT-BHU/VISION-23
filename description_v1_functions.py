"""
env.move(vels)
Function Description: 
    Arguments:
        vels: 2 dimensional list
                vels = [[v1, v2],
                        [v3, v4]]
                v1 - velocity of front_left wheel
                v2 - velocity of front_right wheel
                v3 - velocity of backward_left wheel
                v4 - velocity of backward_right wheel
    Returns:
        None
"""

"""
env.open_grip(delay)
Function Description: 
    Arguments:
        delay: float value
                It is time given to gripper to open its arms
                Default value is 1./240. sec        
    Returns:
        None
"""

"""
env.close_grip(delay)
Function Description: 
    Arguments:
        delay: float value
                It is time given to gripper to close its arms
                Default value is 1./240. sec        
    Returns:
        None
"""

"""
env.get_image(cam_height, dims)
Function Description: 
    Arguments:
        cam_height: float value
                It is height above which camera is attached to the car
                Default value is 0 m
        dims: 1 dimension array
                It is the dimensions of image you want to get     
    Returns:
        bgr image
"""

"""
env.shoot(force)
Function Description: 
    Arguments:
        force: float value
            It is the force by which the shaft attached to car moves  
    Returns:
        None
"""