from setuptools import setup

setup(
    name='gamify',
    version='v0.0.1',
    long_description=__doc__,
    packages=['gamify'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)