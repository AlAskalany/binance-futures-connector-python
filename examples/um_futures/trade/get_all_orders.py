#!/usr/bin/env python
import json
import logging
import os
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = os.environ['API_KEY']
secret = os.environ['API_SECRET']

um_futures_client = UMFutures(key=key, secret=secret, base_url="https://testnet.binancefuture.com")

try:
    response = um_futures_client.get_all_orders(symbol="BTCUSDT", recvWindow=2000)
    logging.info(json.dumps(response, indent=2))
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
