from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as README_FILE:
    long_description = README_FILE.read()

setup(
    name="kblang",
    version="0.1.0",
    author="tahairavani",
    author_email="taha.iravani1@gmail.com",
    description="A Python library to correct spelling errors caused by incorrect language selection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tahairavani/kblang",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        
    ],
)
