from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='zmqnect',
      version=version,
      description="Zeromq Publisher and reciever for openkinect",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ben Ford',
      author_email='ben@boothead.co.uk',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      pub = zmqnect.pub:run
      sub_depth = zmqnect.sub:run_depth
      sub_rgb = zmqnect.sub:run_rgb
      """,
      )
