# importing module located in parent folder
import sys
sys.path.insert(0, '../')

import sys
import pyorcid
authors = pyorcid.search('family-name:wilbanksTestName+AND+given-names:john')
#authors = pyorcid.search('family-name:wilbanks+AND+given-names:john')

try:
    first = next(authors)
except StopIteration as ex:
   print('No authors found')
   sys.exit(0)

print(first.family_name)
for author in authors:
    print(author.family_name)
