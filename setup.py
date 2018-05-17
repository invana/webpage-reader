from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='webpage-reader',
    version='0.0.1',
    packages=['webpage_reader'],
    url='https://github.com/invanatech/webpage-reader',
    license='MIT License',
    author='rrmerugu',
    author_email='rrmerugu@gmail.com',
    description='Reads a webpage and extracts the information out of it, based on the HTML5 tags/classes ',
    install_requires=reqs
)
