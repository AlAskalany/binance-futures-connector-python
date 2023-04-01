#!/usr/bin/env python
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
    response = um_futures_client.aysnc_download_info(downloadId="1")
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
