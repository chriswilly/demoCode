from setuptools import setup
__version__ = None
exec(open('nameSurvey/version.py').read())


setup(name='nameSurvey',
      version=__version__,
      description='US SSA registration name dataset',
      url='https://github.com/chriswilly/demoCode/tree/main/nameSurvey',
      author='michael willy',
      author_email='michael dot willy at gmail dot com',
      license='MIT',
      packages=['nameSurvey'],
      zip_safe=False)
