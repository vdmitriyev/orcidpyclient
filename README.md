## About

A simple wrapper around the orcid.org API. Ready to run examples can be found in the ```examples``` folder.

## Installation

### Using pip

Install latest relased version
```
pip install -i https://test.pypi.org/simple/ orcidpyclient
```

Install latest version from source code
```
pip install git+https://github.com/vdmitriyev/orcidpyclient.git
```

### Manual

* Download from the [GitHub](https://github.com/vdmitriyev/orcidpyclient/archive/master.zip) latest version
* Unzip archive
* Create *virtualenv* (```scripts/cmdInitiateEnv.bat```)
* Activate *virtualenv* (```scripts/cmdStartEnv.bat```)
* Run Example

## Examples

#### Command Line Examples

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

### Searching Example

If you'd rather search for authors, try ORCID's search functionality using its
[API specification](https://members.orcid.org/api/tutorial/search-orcid-registry) :

    >>> #do a simple author search for john
    >>> authors = orcidpyclient.search('family-name:wilbanks+AND+given-names:john')
    >>> print (next(authors).family_name)
    wilbanks

#### Ready to Run Examples

* Examples could be found in the folder [examples](examples)

## Development

* Create virtualenv using ```scripts/cmdInitiateEnv.bat``` and activate it
* Star VS Code
```
code .
```
* Run tests -> pytest
```
cd tests
pytest
```
* Run tests -> tox
```
tox
tox -e py310
```

## License 

MIT 

## Credits

* Created based on the cloned repository https://github.com/scholrly/orcid-python lead by [Matt Luongo](https://github.com/mhluongo) from [Scholrly](https://github.com/scholrly/)
