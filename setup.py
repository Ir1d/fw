import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fw",
    version="0.0.10",
    author="Ir1d",
    author_email="sirius.caffrey@gmail.com",
    description="Easy2use framework to organize experiments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ir1d/fw",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
