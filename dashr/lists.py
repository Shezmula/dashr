class Lists(object):
    """Interface to the Dasher.tv Squares API
    Args:
        client (Client): The dashr client to be used for requests
    """

    def __init__(self, client):
        self._client = client

    def details(self, square_id):
        """Returns the details of a given square."""
        return self._client.request('/squares/info', {'square': square_id})

    def edit(self, square_id, key, value):
        """Updates a property of a given list."""
        params = {
            'square': square_id,
            'list_item': key,
            'properties': value

        }
        return self._client.request('/lists/edit', params)

    def delete(self, square_id, key):
        """Updates a property of a given list."""
        params = {
            'square': square_id,
            'list_item': key

        }
        return self._client.request('/lists/delete', params)
