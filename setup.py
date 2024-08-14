from setuptools import setup, find_packages

setup(
    name='dsplayer-plugin',  
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'dsplayer'
    ],
    entry_points={
        'dsplayer.plugins': [
            'plugin = plugin.plugin:Plugin',
        ],
    },
)