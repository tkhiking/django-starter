import subprocess

from setuptools import Command, setup

PACKAGE_NAME = "django-starter"
VERSION = "0.1.0"


class BaseCommand(Command):
    description = ""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class VetCommand(BaseCommand):
    def run(self):
        subprocess.call(["flake8"])
        subprocess.call(["mypy", "."])


class FormatCommand(BaseCommand):
    def run(self):
        subprocess.call(["black", "."])
        subprocess.call(["isort", "-y"])


class FormatCheckCommand(BaseCommand):
    def run(self):
        subprocess.call(["black", "--check", "."])
        subprocess.call(["isort", "-c"])


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    packages=[PACKAGE_NAME],
    cmdclass={"vet": VetCommand, "fmt": FormatCommand, "fmtchk": FormatCheckCommand},
)
