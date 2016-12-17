# -*- coding: utf-8 -*-

import requests
import json


class Client(object):
    """Base request handler for the Dasher.tv API

    Args:
        api_token (str): Your Dasher.tv API token
    """

    def __init__(self, api_token):
        self.api_token = api_token

    def request(self, path, params={}):
        """Makes a request to the Dasher.tv API"""
        try:
            response = requests.get(
                url=self._url(path),
                headers={
                    "X-Auth-Token": self.api_token,
                    "Content-Type": "application/json",
                },
                data=json.dumps(params)
            )
            json_data = response.json()
            if json_data['status'] == 'success':
                return json_data
            else:
                raise APIError(json_data['status'], path, json_data['data']['message'])

        except requests.exceptions.RequestException as e:
            raise e

    def _url(self, path):
        """Returns the full API url for a given path"""
        return 'https://dasher.tv/api/v1' + path


class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status, path, message):
        self.status = status
        self.message = message
        self.path = path

    def __str__(self):
        return "APIError [{status}]: GET {path}: {message} ".format(path=self.path, status=self.status, message=self.message)
