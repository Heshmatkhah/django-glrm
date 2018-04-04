import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-glrm',
    version='1.1.2',
    packages=find_packages(),
    include_package_data=True,
    license='Apache Software License', 
    description='A Django middleware that make all views and URLs login required.',
    long_description=README,
    project_urls={
        'Documentation': 'http://django-glrm.readthedocs.io/',
        'Source': 'https://github.com/MA-Heshmatkhah/django-glrm/',
        'Tracker': 'https://github.com/MA-Heshmatkhah/django-glrm/issues',
    },
    author='M.A. Heshmatkhah',
    author_email='maheshmatkhah.prg@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',  
        'Framework :: Django :: 1.11',  
        'Framework :: Django :: 2.0',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',  
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)