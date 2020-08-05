import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Hencoder",
    version="1.0.0",
    author="Akash Tyagi",
    author_email="akashtyagi.ta@gmail.com",
    description="An text encoder based on Hauffman Encoding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Akashtyagi08/Hencoder",
    license = 'MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
    test_suite="nose.collector",
    tests_require=["nose"],
    keywords = ['Hauffman', 'encoder', 'decoder','Encoding','decoding'],
)
