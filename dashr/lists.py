class Lists(object):
    """Interface to the Dasher.tv Lists API
    Args:
        client (Client): The dashr client to be used for requests
    """

    def __init__(self, client):
        self._client = client

    def details(self, square_id):
        """Returns the details of a given square."""
        return self._client.request('/squares/info', {'square': square_id})

    def add(self, square_id, key, value, index_value):
        """Adds a value of a given list."""
        params = {
            'square': square_id,
            'list_item': key,
            'properties': value,
            'index': index_value

        }
        return self._client.request('/lists/add', params)

    def edit(self, square_id, key, value):
        """Updates a property of a given list."""
        params = {
            'square': square_id,
            'list_item': key,
            'properties': value

        }
        return self._client.request('/lists/edit', params)
    
    def replace(self, square_id, list_array):
        """Updates a property of a given list."""
        params = {
            'square': square_id,
            'items': list_array

        }
        return self._client.request('/lists/replace', params)

    def delete(self, square_id, key):
        """Updates a property of a given list."""
        params = {
            'square': square_id,
            'list_item': key

        }
        return self._client.request('/lists/delete', params)
