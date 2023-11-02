import sys

try:
    import pyorcid
except:
    sys.path.append('../')
    import pyorcid

def test_orcid_api_version():
    assert pyorcid.orcid_api_version() == '3.0'

def test_existing_name():
    expected = 'wilbanks'
    authors = pyorcid.search('family-name:wilbanks+AND+given-names:john')
    
    assert (next(authors).family_name) == expected

def test_existing_name_object():
    expected = '<Author b\'john\' b\'wilbanks\', ORCID 0000-0002-4510-0385>'
    orcid_res = pyorcid.get('0000-0002-4510-0385')

    assert str(orcid_res) == expected

def test_non_existing_name():

    authors = pyorcid.search('family-name:wilbanksTestName+AND+given-names:john', verbose=True)
    expected = 'No authors found'
    found = None
    
    try:
        first = next(authors)
    except StopIteration as ex:
       found = expected
    assert expected == found 

def test_keywords():
    
    keywords_expected = ['big data', 'machine learning', 'data mining', 'databases', 'data analysis', 'user-defined functions']

    orcid_res = pyorcid.get('0000-0001-5661-4587')
    keywords_orcid =  orcid_res.keywords
    
    keywords_expected.sort()
    keywords_orcid.sort()
    
    assert keywords_expected == keywords_orcid
