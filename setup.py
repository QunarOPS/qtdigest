from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qtdigest',
    version='0.3.1',
    description='python implementation of Dunning\'s T-Digest',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    install_requires=['bintrees>=2.0.0,<=2.0.7'],
    extras_require={
        'test': ['pytest', 'pytest-cov'],
    },
    package_data={
        'qtdigest': ['../README.md'],
    }
)
