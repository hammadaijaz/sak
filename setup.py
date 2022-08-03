from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sak/__init__.py
from sak import __version__ as version

setup(
	name="sak",
	version=version,
	description="For HR and Payroll",
	author="SRCA",
	author_email="hammad@srca.ai",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
