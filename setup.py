from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pyorcid',
      version='0.2',
      description='A simple wrapper around the ORCID.org API.',
      long_description=readme(),
      classifiers=[
                  'Development Status :: 4 - Alpha',
                  'License :: OSI Approved :: MIT License',
                  ],
      url='https://github.com/vdmitriyev/py-orcid',
      author='Matt Luongo, Viktor Dmitriyev',
      author_email='mhluongo@gmail.com',
      license='MIT',
      packages=['pyorcid'],
      install_requires=[
                      'requests>=1.0.4',
                  ]
     )
