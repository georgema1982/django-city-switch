from setuptools import setup, find_packages
setup(
    name = "django-city-switch",
    version = "0.1.0",
    packages = find_packages(),
    author = "George Ma",
    author_email = "george.ma1982@gmail.com",
    description = "In location based social network, it's common to allow users to switch between different cities to see different contents. This project provides a framework to implement this requirement. A default implementation is included.",
    long_description = """
        In location based social network, it's common to allow users to switch between different cities to see different contents. This project provides a framework to implement this requirement. A default implementation is included
    """,
    license = "BSD",
    keywords = "django,city",
    url = "https://github.com/georgema1982/django-city-switch",
    include_package_data=True,
    zip_safe=False,
)

