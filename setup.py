from setuptools import setup, find_packages

setup(
    name='stable-diffusion',
    version='0.0.1',
    description='',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
        'omegaconf',
        'einops',
        'pytorch-lightning==1.9.5',
        'kornia',
        'open_clip_torch',
    ],
)