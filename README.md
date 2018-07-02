### About

A simple wrapper around the orcid.org API. Enhanced clone of this rep - https://github.com/scholrly/orcid-python. Ready to run examples can be found in the [examples](examples) folder.

### Install

Install at once with pip
```
pip install git+https://github.com/vdmitriyev/pyorcid.git
```

Manual installation (or usage):
* Download from the [GitHub](https://github.com/vdmitriyev/pyorcid/archive/master.zip) latest version
* Unzip archive
* Install dependencies (see the section *Dependencies*)

### Dependencies

* requests>=1.0.4

Install dependencies with pip
```
pip install -r requirements.txt
```

### Command Line Examples

Here's a quick snippet to get info on `John Wilbanks`_. ::

    >>> import pyorcid
    >>> #retrieve john's profile from his ORCID
    >>> john = pyorcid.get('0000-0002-4510-0385')
    >>> print john.family_name
    wilbanks

What if you'd like to see an author's works or areas of interest? ::

    >>> print john.keywords
    []
    >>> print john.publications
    []

Hm, let's try another author. ::

    >>> alfonso = orcid.get('0000-0001-8855-5569')
    >>> print alfonso.keywords
    [u'computer science', u' bioinformatics', u' computational biology']
    >>> print alfonso.publications[0]
    <Publication "A note about norbert wiener and his contribution to harmonic analysis and tauberian theorems">


Maybe you'd like to read about Mr. Wiener's contributions? ::

    >>> print alfonso.publications[0].url
    http://www.scopus.com/inward/record.url?eid=2-s2.0-67650513866&partnerID=MN8TOARS

### Searching


If you'd rather search for authors, try ORCID's search functionality using its
[API specification](https://members.orcid.org/api/tutorial/search-orcid-registry) :

    >>> #do a simple author search for john
    >>> authors = orcid.search('family-name:wilbanks+AND+given-names:john')
    >>> print next(authors).family_name
    wilbanks

### Credits

Cloned from the repository https://github.com/scholrly/orcid-python lead by [Matt Luongo](https://github.com/mhluongo) from [Scholrly](https://github.com/scholrly/)
