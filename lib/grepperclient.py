import requests
import asyncio
from base64 import b64encode
from enum import Enum


async def basic_auth(username):
    """
    Should not be called outside of Client.
    Function modified from: https://stackoverflow.com/a/7000784/15982771


    :param username: String of the token that's used to authenticate the Client
    :return: The token from base64
    """
    token = b64encode(f"{username}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'


def create_client(secret: str):
    """
    Helper function to create the client really quickly with asyncio.
    :param secret: The client secret required to create the client.
    :return: Client.
    """
    client = Client()
    asyncio.run(client.authenticate(secret))
    return client


class Client:
    def __init__(self):
        """
        The client should only be created once.
        """
        self.authenticated = False

    # @staticmethod TODO: Implement error handling
    # async def handle_errors(request: int):
    #     if request == 200:
    #         return ""
    #     elif request ==

    async def authenticate(self, secret: str):
        """
        Called automatically in `__init__`. Does not need to be called again.

        :param secret:
        :return: None
        """

        req = requests.get('http://api.grepper.com', auth=(secret, '')).status_code
        # TODO: Error handling
        return req
