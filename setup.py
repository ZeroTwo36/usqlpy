from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='usqlpy',
  version='0.2.1',
  description='A Python wrapper for uSQL',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  url='',  
  author='ZeroTwo36 ',
  author_email='zerotwo36@protonmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='sql db usql', 
  packages=find_packages(),
  install_requires=['requests'] 
)
