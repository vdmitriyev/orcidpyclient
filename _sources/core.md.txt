## Getting started

How to install the package: [installation](installation.md)

### Basics Usage

#### A quick snippet to get info on the author

The name of the author ```John Wilbanks```

```python
import orcidpyclient
orcid_res = orcidpyclient.get('0000-0002-4510-0385')
print (orcid_res.family_name)
```

Expected output:
```bash
wilbanks
```

#### See an author's works or areas of interest

```python
import orcidpyclient
orcid_res = orcidpyclient.get('0000-0002-4510-0385')
print(orcid_res.keywords)
print(orcid_res.publications)
```
#### Iterate over keywords

```python
import orcidpyclient
orcid_res = orcidpyclient.get('0000-0002-4510-0385')
for key_word in orcid_res.keywords:
    print (key_word)
```

#### Iterate over publications

```python
import orcidpyclient
orcid_res = orcidpyclient.get('0000-0002-4510-0385')
for value in obj.publications:
    print(value)
```

#### Trying different author with a different ORCID

```python
import orcidpyclient
author = orcidpyclient.get('0000-0001-8855-5569')
print (author.keywords)
print (author.publications[0])
```

Expected output:

```bash
$ [u'computer science', u' bioinformatics', u' computational biology']
$ <Publication "A note about norbert wiener and his contribution to harmonic analysis and tauberian theorems">
```

#### Getting infos on author's contributions:

```python
import orcidpyclient
author = orcidpyclient.get('0000-0001-8855-5569')
print(author.publications[0].url)
````

Expected output:
```bash
$ http://www.scopus.com/inward/record.url?eid=2-s2.0-67650513866&partnerID=MN8TOARS
```

#### Different ways to run orcid search (e.g., by author's name)

##### Search for an author

If you'd rather search for authors, try ORCID's search functionality using its
[API specification](https://members.orcid.org/api/tutorial/search-orcid-registry) :

```python
import orcidpyclient
authors = orcidpyclient.search('family-name:wilbanks+AND+given-names:john')
print (next(authors).family_name)
```
Expected output:
```bash
$ wilbanks
```

##### Search for an author with no ORCID

```python
import orcidpyclient
authors = orcidpyclient.search('family-name:wilbanksTestName+AND+given-names:john')

try:
    first = next(authors)
except StopIteration as ex:
    raise Exception('No authors found')

print(first.family_name)
for author in authors:
    print(author.family_name)
```

##### Search for an author with empty family name

```python
import orcidpyclient

def get_affiliation(orcid:str):
    """Gets affiliation of the"""

    author = pyorcid.get(orcid)
    print(f'Educations   : {author.educations}')
    print(f'Employments  : {author.employments}')
    print(f'Affiliations : {author.affiliations}')

def empty_family_name():
    """"Search for an author with empty family name"""

    authors = import orcidpyclient.search('family-name:wilbanks&start=0&rows=3', verbose=False)
    for author in authors:
        print(f'Author: {author}')
        get_affiliation(orcid = author.orcid)

empty_family_name()
```
