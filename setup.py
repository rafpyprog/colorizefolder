#!python

from setuptools import setup, find_packages

setup(
      # Package metadata
      name='Colorize Folder',
      version='0.1.0',
      url='https://bitbucket.org/derep/sarptools/',
      description='Customize windows folder with color icons',
      author='Rafael Alves Ribeiro',
      author_email='rafael.alves.ribeiro@gmail.com',
      license='MIT',


      packages=find_packages(),
      package_data={'colorizefolder': ['icons/*.ico']},

      install_requires=['fire >= 0.1.1',],
    )
