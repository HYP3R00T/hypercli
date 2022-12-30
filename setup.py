import setuptools

with open("./README.md", "r") as readme:
    desc = readme.read()

setuptools.setup(
    name="hypercli",
    version="0.1.3",
    author="HYP3R00T",
    author_email="contact@hyperoot.live",
    description="A python based CLI tool",
    url="https://github.com/the-hyperoot/hyper_cli",
    license='MIT',
    packages=['hypercli'],
    zip_safe=False,
    install_requires=['pyfiglet',
                      'rich',
                      'termcolor'
                      ]
)
