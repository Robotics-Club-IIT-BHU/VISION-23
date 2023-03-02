import gym
import os
import time as t
import pybullet as p
import vision_v1

CAR_LOCATION = [-3,0,1.5]
BALLS_LOCATION = dict({
    'red'    : [3,4,1.5],
    'blue' : [4,6,1.5],
    'yellow'   : [-2,6,1.5],
    'green' : [1,-6,1.5]
})
HUMANOIDS_LOCATION = dict({
    'red'    : [6,0,1.5],
    'blue' : [0,6,1.5],
    'yellow'   : [-6,0,1.5],
    'green' : [0,-6,1.5]
})
VISUAL_CAM_SETTINGS = dict({
    'cam_dist'       : 13,
    'cam_yaw'        : 0,
    'cam_pitch'      : -110,
    'cam_target_pos' : [0,4,0]
})

os.chdir(os.path.dirname(os.getcwd()))
env = gym.make('vision-v1', 
    car_location=CAR_LOCATION,
    balls_location=BALLS_LOCATION,
    humanoids_location=HUMANOIDS_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)

t.sleep(100)