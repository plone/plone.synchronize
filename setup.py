from setuptools import setup, find_packages

version = '1.0.4'

setup(
    name='plone.synchronize',
    version=version,
    description="Simple decorators to support synchronized methods",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 6 - Mature",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
    ],
    keywords='synchronized lock decorator',
    author='Martin Aspeli',
    author_email='optilude@gmail.com',
    url='https://pypi.org/project/plone.synchronize',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points="""
    """,
    )
