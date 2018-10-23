from setuptools import setup

setup(name='forge_api_client',
      version='0.1',
      description='Autodesk Forge API client for Python',
      url='http://github.com/dmh126/forge-api-python-client',
      author='Damian Harasymczuk',
      author_email='harasymczuk@contecht.eu',
      license='MIT',
      packages=['forge_api_client'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
