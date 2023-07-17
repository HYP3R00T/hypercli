# ! Don't forget to update the version details in README.md

import setuptools

with open("./README.md", "r") as readme:
    desc = readme.read()

setuptools.setup(
    name="hypercli",
    version="1.0.0",
    author="HYP3R00T",
    author_email="hyperoot@pm.me",
    description="Generate enhanced menu-driven CLI programs with ease!",
    url="https://github.com/HYP3R00T/hypercli",
    long_description=desc,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["hypercli"],
    zip_safe=False,
    install_requires=["pyfiglet", "rich", "termcolor"],
)
