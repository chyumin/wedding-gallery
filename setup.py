from setuptools import setup

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='wedding_gallery',
    version='0.0.1',
    packages=['wedding_gallery'],
    include_package_data=True,
    install_requires=reqs
)
