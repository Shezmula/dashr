# -*- coding: utf-8 -*-

from .client import Client
from .screens import Screens
from .squares import Squares
from .lists import Lists


class Dashr:
    """Base request handler for the Dasher.tv API

    Args:
        api_token (str): Your Dasher.tv API token
    """

    def __init__(self, api_token):
        self._client = Client(api_token)

        self.screens = Screens(self._client)
        self.squares = Squares(self._client)
        self.lists = Lists(self._client)
