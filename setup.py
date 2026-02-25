"""Setup configuration for rail-score (DEPRECATED — redirects to rail-score-sdk)."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rail-score",
    version="2.0.0",
    author="Sumit Verma, Responsible AI Labs",
    author_email="sumit@responsibleailabs.ai",
    description="DEPRECATED — use rail-score-sdk instead. This package redirects to rail-score-sdk.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RAILethicsHub/rail-score/tree/main/python",
    packages=["rail_score"],
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
    install_requires=[
        "rail-score-sdk>=2.1.0",
    ],
)
