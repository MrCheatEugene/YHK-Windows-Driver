"""
This is the setup info for the python installer.
You probably don't need to do anything with it directly.
Just run make and it will be used to create a distributable package
for more info on how this works, see:
    http://wheel.readthedocs.org/en/latest/
    and/or
    http://pythonwheels.com
"""
import typing
from setuptools import setup, Distribution # type: ignore


class BinaryDistribution(Distribution):
    """
    Spec for the distribution
    """
    def is_pure(self):
        """
        Are there os-specific files?
        """
        return False # return False if there is OS-specific files


if __name__ == '__main__':
    import sys
    import os
    here=os.path.dirname(os.path.realpath(__file__))
    sys.path.append(here)
    name='virtualPrinter'
    version='1.0'
    description="""This library allows you to create and register
        a virtual printer using python to process anything the user prints"""
    packages=[name]
    package_data:typing.Dict={ # add all files for a package
        name:[]
    }
    package_dir={name:here}
    distclass=BinaryDistribution
    setup(
        name=name,
        version=version,
        description=description,
        author='kurt',
        author_email='TheHeadlesSourceMan@gmail.com',
        url='https://github.com/TheHeadlessSourceMan/virtualPrinter',
        download_url='https://github.com/TheHeadlessSourceMan/virtualPrinter/archive/1.0.tar.gz', # noqa: E501 # pylint: disable=line-too-long
        keywords=['printer','windows','virtual printer'],
        packages=packages,
        package_dir=package_dir,
        package_data=package_data,
        distclass=distclass)
