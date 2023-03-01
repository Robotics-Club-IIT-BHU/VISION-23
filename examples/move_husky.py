import gym
import os
import time as t
import pybullet as p
import vision_v0
import pybullet as p

os.chdir(os.getcwd())

env = gym.make('vision-v0', 
    car_location=[2,0,1.5]
)

env.move(vels=[[2,2],
               [2,2]])
t.sleep(2)
env.move(vels=[[-2,2],
               [-2,2]])
t.sleep(2)
env.move(vels=[[-2,-2],
               [-2,-2]])
t.sleep(2)