#!/usr/bin/env python
import json
import logging
import os
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

# HMAC authentication with API key and secret
key = os.environ['API_KEY']
secret = os.environ['API_SECRET']

hmac_client = UMFutures(key=key, secret=secret, base_url="https://testnet.binancefuture.com")
logging.info(hmac_client.account(recvWindow=6000))

try:
    response = hmac_client.account(recvWindow=6000)
    logging.info(json.dumps(response, indent=2))
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
