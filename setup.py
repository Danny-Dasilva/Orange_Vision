from setuptools import setup, find_packages

import re

import os
from os import path
package = 'Orange_Vision'

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

init_path = os.path.join(os.path.dirname(__file__),
                         package,
                         '__init__.py')
with open(init_path) as f:
    contents = f.read()
__version__ = re.search(r"__version__ = '([.\d]+)'", contents).group(1)

setup(
    name=package,
    version=__version__,
    description="FRC Orange Vision API",
    long_description=long_description.strip('\n'),
    long_description_content_type='text/markdown', 
    author='Danny Dasilva',
    author_email='dannydasilva.solutions@gmail.com',
    license='Apache 2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy>=1.12.1',
        'Pillow>=4.0.0',
        'pygobject>=3.22.0',
        'protobuf>=3.0.0',
        'edgetpu',
        'littleutils',
        'requests'
    ],
    scripts = [
        'scripts/kill.sh',
        'scripts/autoboot.sh',
        'scripts/wifi_down.sh',
        'scripts/wifi_up.sh'
    ],
    entry_points = {
        'console_scripts': ['orange_classify=Orange_Vision.classify:main',
                            'orange_classify_server=Orange_Vision.classify_server:main',
                            'orange_detect=Orange_Vision.detect:main',
                            'orange_detect_server=Orange_Vision.detect_server:main'],
    },
    python_requires='>=3.5.3',
)
