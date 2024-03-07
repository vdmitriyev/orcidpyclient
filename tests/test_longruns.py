import sys
import pytest

try:
    import pyorcid
except:
    sys.path.append("../")
    import pyorcid


@pytest.mark.skip(reason="long run test")
def test_publication():

    cnt_publications = 22

    orcid_res = pyorcid.get("0000-0001-5661-4587")
    cnt_publications_orcid = len(orcid_res.publications)

    assert cnt_publications == cnt_publications_orcid
