from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), 'rb') as f:
    long_description = f.read().decode('utf-8')

with open("%s/stacklog/VERSION" % this_directory) as f:
     version = f.read().strip('\n')

setup(
  name = 'stacklog',
  packages = ['stacklog'],
  package_data={'': ['VERSION']},
  version = version,
  description = 'A Python Package for Sending Logs to StackLog',
  author = 'StackLog Inc.',
  author_email = 'help@stacklog.io',
  license = 'MIT',
  url = 'https://github.com/appgurung/StackLogPython',
  download_url = ('https://github.com/appgurung/StackLogPython/tarball/%s' %(version)),
  keywords = ['stacklog', 'logging', 'logs', 'python', 'stacklog.io', 'logger'],
  install_requires=[
    'requests',
  ],
  classifiers = [],
  long_description=long_description,
  long_description_content_type='text/markdown',
)
