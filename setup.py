from setuptools import setup

setup(
        name='pyflock',
        version='0.1',
        description='Python client for flockOS',
        url='https://github.com/talk-to/pyflock',
        author='Balajiganapathi S',
        author_email='balajiganapathi@riva.co',
        packages=['pyflock'],
        install_requires=[
            'PyJWT', 
            'requests'
        ],
        zip_safe=False)

