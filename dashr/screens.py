# -*- coding: utf-8 -*-


class Screens:
    """Interface to the Dasher.tv Screens API

    Args:
        client (Client): The dashr client to be used for requests
    """

    def __init__(self, client):
        self._client = client

    def list(self):
        """Returns a list of screens."""
        return self._client.request('/screens/list')

    def details(self, screen_id):
        """Returns the details of a given screen."""
        return self._client.request('/screens/details', {'id': screen_id})
