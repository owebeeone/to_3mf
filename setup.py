from setuptools import setup, find_packages

setup(
    name="to_3mf",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
) 