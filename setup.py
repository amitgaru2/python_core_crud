from distutils.core import setup

setup(
        name='Assignment 1',
        version='1.0',
        description='Task 1 / Assignment 1 / CRUD / SORTING / SEARCHING / SQLITE / POSTGRES',
        author='Amit Garu',
        author_email='amitgaru2@gmail.com',
        url='http://github.com/arneec',
        packages=['src','media'],
        install_requires=[
                'psycopg2-binary==2.7.4',
        ],
     )
