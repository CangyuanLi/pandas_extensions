import setuptools

setuptools.setup(
    name="custom_pandas_extensions",
    version="0.0.1",
    author="Cangyuan Li",
    author_email="everest229@gmail.com",
    description="Adds methods to pandas",
    url="https://github.com/CangyuanLi/pandas_extensions",
    packages=["pandas_extensions"],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)