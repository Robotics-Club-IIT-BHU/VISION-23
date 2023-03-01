import gym
import os
import time as t
import pybullet as p
import vision_v0
import pybullet as p

os.chdir(os.getcwd())

env = gym.make('vision-v0', 
    car_location=[2,0,1.5],
    ball_location=[-2,0,1.5],
    humanoid_location=[-6,0,1.2],
    visual_cam_settings=dict({
        'cam_dist'       : 13,
        'cam_yaw'        : 0,
        'cam_pitch'      : -110,
        'cam_target_pos' : [0,4,0]
    })
)

env.open_grip()
env.move(vels=[[2,2],
               [2,2]])
t.sleep(3.5)
env.move(vels=[[0,0],
               [0,0]])
env.close_grip()
t.sleep(1)
env.open_grip()
t.sleep(1)
env.shoot(100)
t.sleep(3)