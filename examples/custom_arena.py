import gym
import os
import time as t
import pybullet as p
import vision_v0
import pybullet as p

os.chdir(os.getcwd())

CAR_LOACTION = [2,3,1.5]
BALL_LOACTION = [4,5,1.5]
HUMANOID_LOCATION = [-3,-4,1.3]
VISUAL_CAM_SETTINGS = dict({
    'cam_dist'       : 13,
    'cam_yaw'        : 0,
    'cam_pitch'      : -110,
    'cam_target_pos' : [0,4,0]
})

env = gym.make('vision-v0', 
    car_location=CAR_LOACTION,
    ball_location=BALL_LOACTION,
    humanoid_location=HUMANOID_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)

t.sleep(10)