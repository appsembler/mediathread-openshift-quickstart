import os
from setuptools import setup, find_packages
from pip.req import parse_requirements

#REQUIREMENTS_FILE = os.path.join( os.path.dirname(__file__), 'requirements.openshift.txt')

PROJECT_NAME = '<your-project-name>'
AUTHOR_NAME = '<your-name>'
AUTHOR_EMAIL = '<your-email-address>'
PROJECT_URL = ''
DESCRIPTION = '<your-project-description>'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

#REQUIREMENTS = [ str(ri.req) for ri in parse_requirements(REQUIREMENTS_FILE) ]

setup(name=PROJECT_NAME,
	version='1.0',
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    url=PROJECT_URL,
	packages=find_packages(),
	include_package_data=True,
    description=DESCRIPTION,
    #    install_requires=REQUIREMENTS)
    )
