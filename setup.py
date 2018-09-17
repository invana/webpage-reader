from setuptools import setup

with open('requirements.txt', 'r') as f:
    install_reqs = [
        s for s in [
            line.strip(' \n') for line in f
        ] if not s.startswith('#') and s != ''
    ]

setup(
    name='webpage-reader',
    version='0.0.4',
    packages=['webpage_reader'],
    url='https://github.com/invanatech/webpage-reader',
    license='MIT License',
    author='rrmerugu',
    author_email='rrmerugu@gmail.com',
    description='Reads a webpage and extracts the information out of it, based on the HTML5 tags/classes ',
    install_requires=[
        "requests==2.18.4",
        "beautifulsoup4==4.6.0",
        "flatten_json==0.1.6"
    ]
)
