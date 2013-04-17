from setuptools import setup
import djapps

setup(
    name='djapps',
    version=djapps.__version__,
    packages=['djapps'],
    license='BSD',
    description='Load your django apps by app name rather than module path.',
    long_description=open('README.rst').read(),
    author='Richard Ward',
    author_email='richard@richard.ward.name',
    url='https://github.com/RichardOfWard/djapps',
    test_suite='testproject.tests',
    tests_require=['django'],
    include_package_data=True,
)
