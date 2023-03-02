import setuptools
from pathlib import Path

setuptools.setup(
    name='vision_v0',
    version='0.6.6',
    description="A OpenAI Gym Env for vision",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include="vision_v0*"),
    install_requires=['gym']
)