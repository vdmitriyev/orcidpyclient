import json
import logging
import sys

import requests

from .constants import BASE_HEADERS, ORCID_API_VERSION, ORCID_PUBLIC_BASE_URL
from .logger_config import logger, stdout_sh
from .rest import Author


def _set_logger_debug(debug: bool = False):
    """_summary_

    Args:
        debug (bool, optional): _description_. Defaults to False.
    """

    if debug:
        logger.setLevel(logging.DEBUG)
        stdout_sh.setLevel(logging.DEBUG)


def get(orcid_id: str, debug: bool = False):
    """Get an author based on an ORCID identifier."""

    _set_logger_debug(debug)

    if sys.version_info[0] < 3:
        raise Exception("Python 2 is not supported")

    _url = f"{ORCID_PUBLIC_BASE_URL}{orcid_id}"
    _res = requests.get(_url, headers=BASE_HEADERS)

    json_body = _res.json()

    logger.debug("RESPONSE (BASE): {0}".format(json.dumps(json_body, sort_keys=True, indent=4, separators=(",", ": "))))

    return Author(json_body)


def search(query, debug: bool = False):
    """Search the ORCID by sending a query to API

       API documentation:
        https://info.orcid.org/documentation/api-tutorials/api-tutorial-searching-the-orcid-registry/

        api_example_query = {'q':'family-name:Malavolti+AND+given-names:Marco'}

    Args:
        query (_type_): query string
        debug (bool, optional): option for the logging. Defaults to False.

    Returns:
        _type_: iterator of the results
    """

    _set_logger_debug(debug)

    if sys.version_info[0] < 3:
        raise Exception("Python 2 is not supported")

    _url = f"{ORCID_PUBLIC_BASE_URL}search?q={query}"
    resp = requests.get(_url, headers=BASE_HEADERS)
    logger.debug(resp.url)
    json_body = resp.json()
    logger.debug(json_body)
    if json_body.get("result") is not None:
        return (get(res.get("orcid-identifier", {}).get("path")) for res in json_body.get("result", {}))
    else:
        return iter(list())


def orcid_api_version():
    """Provides version of ORCID API that is used"""
    return ORCID_API_VERSION
