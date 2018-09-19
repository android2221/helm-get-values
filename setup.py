from setuptools import setup

try:
    from setuptools import setup, find_packages
except ImportError:
    print("setup tools required. Please run: "
          "pip install setuptools).")
    exit()

setup(
    name='helm-get-values',    # This is the name of your PyPI-package.
    version='0.1.1',                          # Update the version number for new releases
    scripts=['get-values'],                 # The name of your scipt, and also the command you'll be using for calling it
    packages=find_packages(),
    install_requires = [
        "click==6.7",
    ]
)