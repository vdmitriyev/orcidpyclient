import requests

from .constants import BASE_HEADERS, ORCID_PUBLIC_BASE_URL
from .logger_config import logger


def _parse_keywords(d):
    if d is not None:
        return [val["content"] for val in d["keyword"]]
    return []


def _parse_affiliations(l):
    """Parses given JSON to get an affiliation (could be education and employment)"""

    _affiliations = []
    if l is not None:
        for d in l:
            name = d["organization"]["name"]
            _affiliations.append(name)
    return _affiliations
