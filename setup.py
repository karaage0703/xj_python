from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='xj_python',
    version='0.1',
    license='MIT',
    description='xj system',
    author='karaage0703',
    url='https://github.com/karaage0703/xj_python',
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt')
)
