import sys
import os
from setuptools import setup
from subprocess import Popen, PIPE
from setuptools.command.install import install


def readme():
    """print long description"""
    with open('README.md') as readme_file:
        return readme_file.read()


def call_git_describe():
    try:
        p = Popen(['git', 'describe', '--tags'],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        return line.strip()

    except:
        return None


def read_release_version():
    try:
        f = open("RELEASE-VERSION", "r")

        try:
            version = f.readlines()[0]
            return version.strip()

        finally:
            f.close()

    except:
        return None


def write_release_version(version):
    f = open("RELEASE-VERSION", "w")
    f.write("%s\n" % version)
    f.close()


def get_git_version():
    # Read in the version that's currently in RELEASE-VERSION.

    release_version = read_release_version()

    # First try to get the current version using "git describe".

    version = call_git_describe()

    # If that doesn't work, fall back on the value that's in
    # RELEASE-VERSION.

    if version is None:
        version = release_version

    # If we still don't have anything, that's an error.

    if version is None:
        raise ValueError("Cannot find the version number!")

    # If the current version is different from what's in the
    # RELEASE-VERSION file, update the file to be current.

    if version != release_version:
        write_release_version(version)

    # Finally, return the current version.

    return version


VERSION = read_release_version()


class VerifyVersionCommand(install):
    """    Custom command to verify the git tag matches the version    """
    description = 'Verify that the git tag matches the version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')
        if tag != VERSION:
            info = "Git tag: {0} does not match the version of app: {1}".format(
                tag, VERSION
            )
            sys.exit(0)


setup(
    name="apitool",
    version=get_git_version(),
    description="CLI utility",
    long_description="Command line utility to do stuff",
    author="Roderick Mackintosh",
    author_email="roderick.mackintosh@gmail.co.nz",
    url="https://github.com/apitool",
    license="Proprietary",
    scripts=["api-tool"],
    packages=['apitool'],
    data_files=[('/etc/apitool', ['data/template.html'])],
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)