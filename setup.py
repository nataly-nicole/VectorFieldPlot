from setuptools import setup, find_packages

setup(
    name='VectorFieldPlot',
    url='https://commons.wikimedia.org/wiki/User:Geek3/VectorFieldPlot#Field_calculation', 
    author='Geek3',
    author_email='https://commons.wikimedia.org/wiki/User:Geek3',
    maintainer='Nataly Nicole Ibarra Vera',
    maintainer_email='natalynicole.ibarravera@gmail.com',
    packages=find_packages(exclude=['notebooks']),
    install_requires=['lxml','matplotlib','scipy'],
    version='3.1',
    license='GPL',
    description='VectorFieldPlot is a python program that creates high quality fieldline plots in the svg vectorgraphics format.',
    long_description=open('README.md').read(),
)
