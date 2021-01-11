import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hey",
    version="0.0.1",
    author="dmitry_muzalevskiy",
    author_email="muzalevsky.ds@gmail.com",
    description="A function that returns 'hey there'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)