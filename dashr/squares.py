# -*- coding: utf-8 -*-


class Squares(object):
    """Interface to the Dasher.tv Squares API

    Args:
        client (Client): The dashr client to be used for requests
    """

    def __init__(self, client):
        self._client = client

    def details(self, square_id):
        """Returns the details of a given square."""
        return self._client.request('/squares/info', {'square': square_id})

    def update(self, square_id, key, value):
        """Updates a property of a given square."""
        params = {
            'square': square_id,
            'key': key,
            'value': value
        }
        return self._client.request('/squares/update_property', params)
