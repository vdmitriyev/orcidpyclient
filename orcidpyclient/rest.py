import json
import unicodedata

import requests

from .constants import BASE_HEADERS, ORCID_PUBLIC_BASE_URL
from .logger_config import logger
from .rest_helpers import _parse_affiliations, _parse_keywords
from .utils import MappingRule as to
from .utils import dictmapper, u


def _parse_researcher_urls(l):
    if l is not None:
        return [Website(d) for d in l]
    return []


def _parse_publications(l):
    _publications = []

    if l is not None:
        # logger.debug(json.dumps(l, sort_keys=True, indent=4, separators=(',', ': ')))
        # getting through all works
        for _, d in enumerate(l):
            path = d["work-summary"][0]["path"]
            _url = "{0}{1}".format(ORCID_PUBLIC_BASE_URL, path[1:])  # remove first symbol '/'
            _res = requests.get(_url, headers=BASE_HEADERS)
            _json_body = _res.json()
            logger.debug(
                "REQUEST (PUBLICATIONS): {0}".format(
                    json.dumps(_json_body, sort_keys=True, indent=4, separators=(",", ": "))
                )
            )
            _publications.append(Publication(_json_body))

    return _publications


AuthorBase = dictmapper(
    "AuthorBase",
    {
        #'orcid'            :['orcid-profile','orcid-identifier','path'],
        "orcid": ["orcid-identifier", "path"],
        "family_name": ["person", "name", "family-name", "value"],
        "given_name": ["person", "name", "given-names", "value"],
        "biography": ["person", "biography", "content"],
        "keywords": to(["person", "keywords"], _parse_keywords),
        "researcher_urls": to(["person", "researcher-urls", "researcher-url"], _parse_researcher_urls),
        "educations": to(["activities-summary", "educations", "education-summary"], _parse_affiliations),
        "employments": to(["activities-summary", "employments", "employment-summary"], _parse_affiliations),
    },
)

Works = dictmapper(
    "Works",
    {
        "publications": to(["group"], _parse_publications),
    },
)

PublicationBase = dictmapper(
    "PublicationBase",
    {
        "title": ["title", "title", "value"],
        "url": ["external-ids", "external-id", "external-id-url"],
        #'citation'      : to(['citation'], lambda l: map(CitationBase, l) if l is not None else None),
        "citation_value": ["citation", "citation-value"],
        "citation_type": ["citation", "citation-type"],
        "publicationyear": ["publication-date", "year", "value"],
    },
)

ExternalIDBase = dictmapper(
    "ExternalIDBase", {"id": ["work-external-identifier-id", "value"], "type": ["work-external-identifier-type"]}
)

CitationBase = dictmapper("CitationBase", {"type": ["citation-type"], "value": ["citation-value"]})

WebsiteBase = dictmapper("WebsiteBase", {"name": ["url-name"], "url": ["url", "value"]})


class Author(AuthorBase):
    _loaded_works = None

    def _load_works(self):
        _url = "{0}{1}/{2}".format(ORCID_PUBLIC_BASE_URL, self.orcid, "works")
        _res = requests.get(_url, headers=BASE_HEADERS)
        _json_body = _res.json()
        logger.debug(
            "RESPONSE (WORKS): {0}".format(json.dumps(_json_body, sort_keys=True, indent=4, separators=(",", ": ")))
        )
        self._loaded_works = Works(_json_body)

    @property
    def publications(self):
        if self._loaded_works is None:
            self._load_works()
        return self._loaded_works.publications

    @property
    def affiliations(self):
        return self.educations + self.employments

    def __repr__(self):
        obj_repr = "<{} {} {}, ORCID {}>"
        return obj_repr.format(
            type(self).__name__,
            self.given_name.encode("utf-8") if self.given_name else "None",
            self.family_name.encode("utf-8") if self.family_name else "None",
            self.orcid,
        )

    def __str__(self):
        return self.__repr__()


class Website(WebsiteBase):
    def __unicode__(self):
        return self.url

    def __repr__(self):
        return "<%s %s [%s]>" % (type(self).__name__, self.name, self.url)


class Citation(CitationBase):
    def __unicode__(self):
        return self.text

    def __repr__(self):
        return "<%s [type: %s]>" % (type(self).__name__, self.type)


class ExternalID(ExternalIDBase):
    def __unicode__(self):
        return unicodedata(self.id)

    def __repr__(self):
        return "<%s %s:%s>" % (type(self).__name__, self.type, str(self.id))


class Publication(PublicationBase):
    def __repr__(self):
        return '<%s "%s">' % (type(self).__name__, self.title)
