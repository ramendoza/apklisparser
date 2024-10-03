from setuptools import setup

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="apklisparser",
    version="1.0.0",
    packages=["apklisparser"],
    author="Rafael Mendoza",
    author_email="ralexm14@gmail.com",
    description="Apklis apk parser",
    url="https://github.com/ramendoza/apklisparser",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=["pyasn1", "cryptography", "lxml", "Pillow", "wand"],
    python_requires='>=3.6',
)
