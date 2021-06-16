# importing module located in parent folder
import sys
sys.path.insert(0, '../')

import sys
import pyorcid

def non_existing_name():
    ''' Searches for authors with no ORCID'''

    authors = pyorcid.search('family-name:wilbanksTestName+AND+given-names:john')

    try:
        first = next(authors)
    except StopIteration as ex:
       print('No authors found')
       sys.exit(0)

    print(first.family_name)
    for author in authors:
        print(author.family_name)

def empty_family_name():

    authors = pyorcid.search('family-name:wilbanks&start=0&rows=3', verbose=False)
    for author in authors:
        print(author)

#non_existing_name()
empty_family_name()
