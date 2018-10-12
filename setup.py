from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'pymysql'
]

setup(
    name='hackThisPage',
    version='0.1',
    description='A CTF site with three major exploits.',
    author='Ryan Stonebraker',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
