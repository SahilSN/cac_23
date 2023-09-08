from setuptools import setup,find_packages

setup(
    name='cac_23',
    version='1.0',
    long_description=__doc__,
    packages=['build'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)