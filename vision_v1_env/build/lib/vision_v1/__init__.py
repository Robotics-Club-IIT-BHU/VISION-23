from gym.envs.registration import register

register(
    id='vision-v1',
    entry_point='vision_v1.envs:VisionEnv',
)