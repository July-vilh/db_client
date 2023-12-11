from setuptools import setup
REQUIRES = [
    'sqlalchemy',
    'records',
    'structlog'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/July-vilh/db_client.git',
    license='MIT',
    author='Yuliya Vilchynskaya',
    install_requires=REQUIRES,
    author_email='-',
    description='DB client info'
)
