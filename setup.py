import setuptools
import os

setuptools.setup(
    name="time_series_DNB",
    version="0.2",
    author="Yuji Okamoto",
    author_email="yuji.0001@gmail.com",
    description="DNB library for long time series data",
    long_description="DNB library for long time series data",
    long_description_content_type="text/markdown",
    url="https://github.com/yuji0001/time_series_DNB",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "dnb_ts = dnb_tools.dnb_ts:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
)