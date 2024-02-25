from setuptools import setup


def get_long_description() -> str:
    content = None
    with open("README.md", "r") as f:
        content = f.read()
    return content


setup(
    name="orcidpyclient",
    version="1.1",
    description="A simple wrapper around the ORCID.org API",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/vdmitriyev/orcidpyclient",
    author="vdmitriyev, Matt Luongo",
    license="MIT",
    packages=["orcidpyclient"],
    install_requires=[
        "requests>=2.28.0",
    ],
)
