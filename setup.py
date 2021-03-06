#-*- coding: utf-8 -*-

"""Polaris setup"""

import os
import sys
import inspect
import shutil

from setuptools import setup, find_packages

VERSION = '0.3.2'

INSTALL_PREFIX = os.path.join('/opt', 'polaris')

# determine the directory where setup.py is located
PWD = os.path.abspath(
    os.path.split(inspect.getfile(inspect.currentframe()))[0])

setup(
    version=VERSION,
    author='Anton Gavrik',    
    name='polaris-gslb',
    description=('A simple, extendable Global Server Load Balancing(GSLB) '
                 'solution, DNS-based traffic manager.'),
    packages = find_packages('.'),
    install_requires=[
        'pyyaml',
        'python3-memcached', 
        'python-daemon-3K'
    ],
    license='BSD 3-Clause',
    url='https://github.com/polaris-gslb/polaris-gslb',
    download_url=('https://github.com/polaris-gslb/polaris-gslb/tarball/v{}'
                  .format(VERSION)),
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)

# create directory topology
for path in [ 
        os.path.join(INSTALL_PREFIX, 'etc'),
        os.path.join(INSTALL_PREFIX, 'bin'),
        os.path.join(INSTALL_PREFIX, 'run'),        
        ]:
    try:
        os.makedirs(path)
    except FileExistsError:
        continue

def copy_files(src_dir, dst_dir):
    """Copy all files from src_dir to dst_dir""" 
    src_files = os.listdir(src_dir)
    for file_name in src_files:
        full_file_name = os.path.join(src_dir, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, dst_dir)

# copy etc/
copy_files(os.path.join(PWD, 'etc'), os.path.join(INSTALL_PREFIX, 'etc'))

# copy bin/
copy_files(os.path.join(PWD, 'bin'), os.path.join(INSTALL_PREFIX, 'bin'))

