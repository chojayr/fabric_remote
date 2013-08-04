import sys
from setuptools import setup

install_requires = ['Flask==0.10.1', 'Fabric==1.6.1']

if sys.version_info < (2, 7):
    install_requires += ['importlib==1.0.2', 'argparse==1.2.1']

setup(
    name='Furoshiki',
    version='0.0.1',
    long_description=__doc__,
    packages=['furoshiki'],
#    include_package_data=True,
#    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts': {
            'furoshiki = furoshiki.main:main'
        }
    }
)

