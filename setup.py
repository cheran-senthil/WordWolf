from setuptools import setup


with open('README.md') as f:
    long_description = f.read()


setup(name='WordWolf',
      version='0.1.0',
      description='Multi-purpose Anagrammer',
      long_description=long_description,
      #long_description_content_type='text/markdown',
      url='https://github.com/Cheran-Senthil/WordWolf',
      author='Cheran',
      license='MIT',
      packages=['wordwolf'],
)
