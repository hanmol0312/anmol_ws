from setuptools import find_packages, setup
from glob import glob
import os
package_name = 'bot_world'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'worlds'),glob('worlds/*')),
        (os.path.join('share',package_name,'launch'),glob('launch/*')),
        (os.path.join('share',package_name,'urdf'),glob('urdf/*')),
        (os.path.join('share',package_name,'meshes'),glob('meshes/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anmol',
    maintainer_email='ec21b1086@iiitdm.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
