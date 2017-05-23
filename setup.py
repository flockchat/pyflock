from setuptools import setup

setup(
        name='flockos',
        version='1.0',
        description='Python client for flockOS',
        url='https://github.com/talk-to/pyflock',
        author='Balajiganapathi S',
        author_email='balajiganapathi@riva.co',
        packages=['flockos'],
        install_requires=[
            'PyJWT', 
            'requests'
        ],
        zip_safe=False)

