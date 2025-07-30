from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='mymath',
      version='0.2',
      description='The best math library',
      url='http://github.com/szabgab/mymath',
      author='Foo Bar',
      author_email='foo@bar.com',
      license='MIT',
      packages=['mymath'],
      zip_safe=False,
      requires=[
          'lawyerup',
      ],
      long_description=readme(),
      scripts=['bin/runmymath.py', 'bin/runmymath.bat'],
      )
