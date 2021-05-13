from setuptools import setup, find_packages

setup(name='myutils',
    version='0.1',
    description='Utilitaire fixant le Python Path',
    url='#',
    author='Boris Bob',
    author_email='borisbob91@gmail.com',
    license='MIT',
    packages=['myutils', 'interface', 'images','models','views'],
    package_dir =  find_packages('src')
    zip_safe=False)
