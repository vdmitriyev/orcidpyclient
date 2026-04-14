## Examples

**Ready to run** examples showing how to use **orcidpyclient** Python package.

#### Script to extract BibTeX from the ORCID

* Script extracts bibtex from the ORCID:  [extracting_bibtex.py](examples/extracting_bibtex.py)

#### Script to convert BibTeX from the ORCID to HTML

* Script to convert BibTeX from the ORCID to HTML: [orcid_bibtex_to_html.py](examples/orcid_bibtex_to_html.py)
* Additional information
	+ iterates through the list or ID's, extracts ORCID, creates bat file to compile bibtex into HTMLs with help of JabRef
		- List should be in the python dict format, here is the example (I created file 'orcid-list.json')
		```json
		[
			{
				"name": "John Wilbanks",
				"orcid": "0000-0002-4510-0385"
			}
		]
		```
    + **NOTE**: To make in run on Mac OS, it's better if you will copy JabRef into the 'generated' folder directly
