from setuptools import setup, find_packages

setup(
    author="Andrew MacLachlan",
    description="A package containing solutions to Project Euler problems",
    name="project_euler",
    version="0.1.0",
    install_requires=[
    ],
    packages=find_packages(include=["project_euler", "project_euler.*"])
)