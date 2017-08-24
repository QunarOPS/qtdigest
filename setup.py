from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='qtdigest',
    version='0.0.2',
    description='python implementation of Dunning\'s T-Digest',
    url='https://github.com/QunarOPS/qtdigest',
    author='zskymn',
    author_email='zsymn@163.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    packages=['qtdigest'],
    install_requires=['bintrees'],
    extras_require={
        'test': ['pytest', 'pytest-cov'],
    },
    package_data={
        'qtdigest': ['../README.md'],
    }
)
