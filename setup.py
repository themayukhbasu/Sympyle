from setuptools import setup, find_packages
import sys

from setuptools.command.test import test as TestCommand

REQUIRES = [
    "numpy"
]
TEST_REQUIRES = [
    "numpy", "pytest", "pytest-cov", "coverage", "pygraphviz"
]


class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):
        import shlex

        # import here, cause outside the eggs aren't loaded
        import pytest
        self.pytest_args = "--cov sympyle"

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name='sympyle',
        version='0.0.12',
        packages=find_packages(),
        url='https://github.com/harveyslash/sympyle',
        license='GNU GENERAL PUBLIC LICENSE',
        author='Harshvardhan Gupta',
        author_email='theharshvardhangupta@gmail.com',
        description='Simple Automatic Differentiation in Python ',
        long_description=long_description,
        long_description_content_type="text/markdown",

        install_requires=REQUIRES,
        tests_require=TEST_REQUIRES,
        cmdclass={"test": PyTest},
)
