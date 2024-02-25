## Getting started

How to install the package: [installation](installation.md)

### Basics

Here's a quick snippet to get info on the author with the name `John Wilbanks`_. :

    >>> import orcidpyclient
    >>> #retrieve john's profile from his ORCID
    >>> orcid_res = orcidpyclient.get('0000-0002-4510-0385')
    >>> print (orcid_res.family_name)
    wilbanks

What if you'd like to see an author's works or areas of interest? :

    >>> print (orcid_res.keywords)
    []
    >>> print (orcid_res.publications)
    []

Try another author with a different ORCID:

    >>> author = orcidpyclient.get('0000-0001-8855-5569')
    >>> print (author.keywords)
    [u'computer science', u' bioinformatics', u' computational biology']
    >>> print (author.publications[0])
    <Publication "A note about norbert wiener and his contribution to harmonic analysis and tauberian theorems">

Read about author's contributions:

    >>> print (author.publications[0].url)
    http://www.scopus.com/inward/record.url?eid=2-s2.0-67650513866&partnerID=MN8TOARS

### Searching

If you'd rather search for authors, try ORCID's search functionality using its
[API specification](https://members.orcid.org/api/tutorial/search-orcid-registry) :

    >>> #do a simple author search for john
    >>> authors = orcidpyclient.search('family-name:wilbanks+AND+given-names:john')
    >>> print (next(authors).family_name)
    wilbanks