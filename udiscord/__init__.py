"""
Author: Xsarz

Enjoy using!
"""

from .utils.objects import *
from .utils import exceptions, log
from .utils.logger import logging
from .ws.event_types import EventType

from .client import Client
#from .async_client import AsyncClient


from os import system as s
from ujson import loads
from requests import get
__title__ = 'udiscord'
__author__ = 'Xsarz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2025 Xsarz'
__version__ = '1.2'


"""
__newest__ = loads(get("https://pypi.org/pypi/python-discord-api/json").text)["info"]["version"]
if __version__ != __newest__:
	s('cls || clear')
	print(f'\033[38;5;214m{__title__} made by {__author__}\nPlease update the library. Your version: {__version__}  A new version:{__newest__}\033[0m')
"""