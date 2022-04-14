from setuptools import setup, find_namespace_packages  # type: ignore
from pathlib import Path

setup(
    name="cleaner_conf",
    version="0.1.4",
    url="https://github.com/cleaner-bot/cleaner-config",
    author="Leo Developer",
    author_email="git@leodev.xyz",
    description="configuration of the cleaner",
    install_requires=Path("requirements.txt").read_text().splitlines(),
    packages=find_namespace_packages(include=["cleaner_conf*"]),
    package_data={"cleaner_conf": ["py.typed"]},
)
