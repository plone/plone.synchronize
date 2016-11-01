from setuptools import setup, find_packages

version = '1.0.2'

setup(
    name='plone.synchronize',
    version=version,
    description="Simple decorators to support synchronized methods",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    # Get more strings from
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
    ],
    keywords='synchronized lock decorator',
    author='Martin Aspeli',
    author_email='optilude@gmail.com',
    url='https://pypi.python.org/pypi/plone.synchronize',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points="""
    """,
    )
