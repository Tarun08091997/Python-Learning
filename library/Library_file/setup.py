from setuptools import setup, find_packages
from my_geometry_library import __version__
setup(
    name='my_geometry_library',
    # sometimes it may happen we use multiple __init__ but want only one package to be included
    packages=find_packages(
        include=['my_geometry_library', 'surface_2D', 'surface_3D']),
    version=__version__,
    description='Python Library for simple Geometric Functions ',
    author='Tarun Kumar',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
