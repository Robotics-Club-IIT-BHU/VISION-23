import gym
import os
import cv2 as cv
import time as t
import pybullet as p
import vision_v0
import pybullet as p

os.chdir(os.getcwd())

env = gym.make('vision-v0', 
    car_location=[2,0,1.2],
    ball_location=[-2,0,1.3]
)

while True:
    img = env.get_image(dims=[600,600])
    cv.imshow("img", img)
    k = cv.waitKey(1)
    if k==ord('q'):
        break