import gym
import os
import cv2 as cv
import time as t
import pybullet as p
import config_v1
import vision_v1

os.chdir(os.path.dirname(os.getcwd()))
env = gym.make('vision-v1', 
    car_location=config_v1.CAR_LOCATION,
    balls_location=config_v1.BALLS_LOCATION,
    humanoids_location=config_v1.HUMANOIDS_LOCATION,
    visual_cam_settings=config_v1.VISUAL_CAM_SETTINGS
)

""" ENTER YOUR CODE HERE """
