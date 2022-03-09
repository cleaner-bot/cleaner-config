from setuptools import setup, find_namespace_packages  # type: ignore

setup(
    name="cleaner_conf",
    version="0.1.0",
    url="https://github.com/cleaner-bot/cleaner-config",
    author="Leo Developer",
    author_email="git@leodev.xyz",
    description="configuration of the cleaner",
    packages=find_namespace_packages(include=["cleaner_conf*"]),
)
