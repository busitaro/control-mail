from setuptools import setup
from setuptools import find_packages


DESCRIPTION = "control mail of microsoft365"
NAME = 'control-mailr'
AUTHOR = 'busitaro10'
AUTHOR_EMAIL = 'busitaro10@gmail.com'
URL = 'https://github.com/busitaro/control-mail'
DOWNLOAD_URL = 'https://github.com/busitaro/control-mail'
VERSION = 0.1

INSTALL_REQUIRES = [
    'beautifulsoup4>=4.9.3',
    'certifi>=2020.12.5',
    'chardet>=4.0.0',
    'idna>=2.10',
    'O365>=2.0.14',
    'oauthlib>=3.1.0',
    'python-dateutil>=2.8.1',
    'pytz>=2021.1',
    'requests>=2.25.1',
    'requests-oauthlib>=1.3.0',
    'six>=1.15.0',
    'soupsieve>=2.2',
    'stringcase>=1.2.0',
    'tzlocal>=2.1',
    'urllib3>=1.26.3',
]

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
)
