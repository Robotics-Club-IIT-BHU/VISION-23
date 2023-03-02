import gym
import os
import cv2 as cv
import time as t
import pybullet as p
import config_v0
import vision_v0

os.chdir(os.path.dirname(os.getcwd()))
env = gym.make('vision-v0', 
    car_location=config_v0.CAR_LOCATION,
    ball_location=config_v0.BALL_LOCATION,
    humanoid_location=config_v0.HUMANOID_LOCATION,
    visual_cam_settings=config_v0.VISUAL_CAM_SETTINGS
)

""" ENTER YOUR CODE HERE """
