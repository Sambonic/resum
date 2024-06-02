from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='resum',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    author='Sambonic',
    description='A quick PDF parser and research summarizer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Sambonic/resum',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
