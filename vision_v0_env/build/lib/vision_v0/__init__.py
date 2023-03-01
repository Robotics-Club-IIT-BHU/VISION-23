from gym.envs.registration import register

register(
    id='vision-v0',
    entry_point='vision_v0.envs:VisionEnv',
)