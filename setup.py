from setuptools import setup, find_packages

setup(
    name="autodocs",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pygments",
        "markdown2",
        "requests",
        "tqdm",  # Add tqdm for progress bars
        # Add other dependencies as needed
    ],
    extras_require={
        "dev": [
            "setuptools",
            "wheel",
            "pylance",
        ],
    },
    entry_points={
        'console_scripts': [
            'autodocs=autodocs.cli:main',
        ],
    },
    author="SLR TECK",
    author_email="ftwenty903@gmail.com",
    description="AutoDocs - Automatic Documentation Generator",
    keywords="documentation, generator, autodocs",
    url="https://github.com/Nom-nom-hub/autodocs",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
