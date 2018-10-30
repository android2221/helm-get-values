from setuptools import setup

try:
    from setuptools import setup, find_packages
except ImportError:
    print("setup tools required. Please run: "
          "pip install setuptools).")
    exit()

setup(
    name='helm-get-values',    # This is the name of your PyPI-package.
    version='0.1.2',                          # Update the version number for new releases
    packages=find_packages(),
    install_requires = [
        "click==6.7",
    ]
)