#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from os import path
from setuptools import setup
import sys

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

    # allow setup.py to be run from any path
    os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__),
                                           os.pardir)))

    data_files_prefix = '/'
    if (getattr(sys, "real_prefix", sys.prefix) != sys.prefix or
        getattr(sys, "base_prefix", sys.prefix) != sys.prefix):
        data_files_prefix = ''

    setup(
        name='ryu-faucet',
        version='1.0',
        packages=['ryu_faucet'],
        package_dir={'ryu_faucet': 'src/ryu_faucet'},
<<<<<<< HEAD
        data_files=[('/etc/ryu/faucet', ['src/cfg/etc/ryu/faucet/gauge.conf',
                                         'src/cfg/etc/ryu/faucet/faucet.yaml',
                                         'src/cfg/etc/ryu/faucet/gauge_db.yaml']),
                    ('/etc/ryu/faucet/upstart', ['src/cfg/etc/ryu/faucet/upstart/gauge.conf',
                                         'src/cfg/etc/ryu/faucet/upstart/faucet.conf',
                                         'src/cfg/etc/ryu/faucet/upstart/gauge',
                                         'src/cfg/etc/ryu/faucet/upstart/faucet'])
                    ],
=======
        data_files=[(data_files_prefix + 'etc/ryu/faucet',
                     ['src/cfg/etc/ryu/faucet/gauge.conf',
                      'src/cfg/etc/ryu/faucet/faucet.yaml'])],
>>>>>>> 377fdd89de6a0737a963af453054c56b5568b4e7
        include_package_data=True,
        install_requires=['ryu', 'pyyaml', 'influxdb', 'ipaddr', 'concurrencytest'],
        license='Apache License 2.0',
        description='Ryu application to perform Layer 2 switching with VLANs.',
        long_description=README,
        url='http://onfsdn.github.io/faucet',
        author='Christopher Lorier',
        author_email='chris.lorier@reannz.co.nz',
        maintainer='Shivaram Mysore, ONFSDN.Org',
        maintainer_email='shivaram.mysore@gmail.com, faucet-dev@OpenflowSDN.Org',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Framework :: Buildout',
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Topic :: System :: Networking',
        ],)
