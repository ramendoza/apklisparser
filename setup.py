from setuptools import setup

setup(
    name="apklisparser",
    version="1.0.0",
    packages=["apklisparser"],
    install_requires=["pyasn1", "cryptography", "lxml", "Pillow", "wand"],
)
