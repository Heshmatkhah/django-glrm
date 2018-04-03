import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djnago-global-login-required-middleware',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License', 
    description='A Django middleware that make all views and URLs login required.',
    long_description=README,
    url='https://www.example.com/',
    author='M.A. Heshmatkhah',
    author_email='maheshmatkhah.prg@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',  
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)