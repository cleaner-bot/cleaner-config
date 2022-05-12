from pathlib import Path

from setuptools import find_namespace_packages, setup  # type: ignore

setup(
    name="cleaner_conf",
    version="0.1.14",
    url="https://github.com/cleaner-bot/cleaner-config",
    author="Leo Developer",
    author_email="git@leodev.xyz",
    description="configuration of the cleaner",
    install_requires=Path("requirements.txt").read_text().splitlines(),
    packages=find_namespace_packages(include=["cleaner_conf*"]),
    package_data={"cleaner_conf": ["py.typed"]},
)
