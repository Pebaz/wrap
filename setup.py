"""
Usage:
pip install git+https://github.com/Pebaz/wrap.git
"""

from setuptools import setup, find_packages

setup(
	name='wrap',
	version='0.1',
	description='Wrap long lines of output in a wide terminal.',
	author='http://github.com/Pebaz',
    py_modules=['wrap'],
	entry_points={
		'console_scripts' : [
			'wrap=wrap:main'
		]
	}
)