from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="siena110jes",
    version="0.0.1",
    author="Red Robin",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Siena110JES/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
)
