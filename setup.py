from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pyorcid',
      version='0.5',
      description='A simple wrapper around the ORCID.org API',
      long_description=readme(),
      classifiers=[
                  'Development Status :: 4 - Alpha',
                  'License :: OSI Approved :: MIT License',
                  ],
      url='https://github.com/vdmitriyev/pyorcid',
      author='Viktor Dmitriyev, Matt Luongo',
      author_email='mhluongo@gmail.com',
      license='MIT',
      packages=['pyorcid'],
      install_requires=[
                      'requests>=1.0.4',
                  ]
     )
