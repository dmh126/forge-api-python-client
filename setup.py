from setuptools import setup

setup(name='forge_data_management_api',
      version='0.1',
      description='Autodesk Forge Data Management API client',
      url='http://github.com/dmh126/forge-python-data-management-api',
      author='Damian Harasymczuk',
      author_email='harasymczuk@contecht.eu',
      license='MIT',
      packages=['forge_data_management_api'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
