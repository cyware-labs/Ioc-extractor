from setuptools import setup, find_packages

requirement = [
    '''bs4
    ioc-finder
    urllib3
    '''
]

setup(
    name="ioc_extractor",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ioc_extractor=ioc_extractor.ioc_extractor:ioc_extractor']
    },
    install_requires=requirement
)