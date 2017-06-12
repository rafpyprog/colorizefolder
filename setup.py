import os
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# Version Number
with open(os.path.join(os.path.dirname(__file__), 'colorizefolder', '__init__.py')) as f:
    version = re.compile(r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)


setup(
      # Package metadata
      name='Colorize Folder',
      version=version,
      url='https://bitbucket.org/derep/sarptools/',
      description='Customize windows folder with color icons',
      author='Rafael Alves Ribeiro',
      author_email='rafael.alves.ribeiro@gmail.com',
      license='MIT',

      include_package_data=True,
      packages=find_packages(),
      package_data={'colorizefolder': ['icons/*.ico']},

      install_requires=['fire >= 0.1.1',],
      entry_points={
        'console_scripts': [
            'colorizefolder = colorizefolder:colorizefolder.main',
        ],
      }
    )
