import os
from lib import grepperclient

client = grepperclient.create_client(str(os.getenv('TOKEN')))  # secret environment variable for the token
