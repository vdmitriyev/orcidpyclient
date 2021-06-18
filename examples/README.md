### About

'Ready to run' examples showing how to use **pyorcid** python module.

### How to run examples

* To run the examples no installation of **pyorcid** module is required.
* Download latest package from [github](https://github.com/vdmitriyev/pyorcid) and unzip it (or use ```git clone```)
* Install dependencies (see file 'requirements.txt')
* Navigate to the folder 'examples'
* For instance, to run **extracting_bibtex.py** use the following command:
```
python extracting_bibtex.py
```

### Examples

* [extracting_bibtex.py](extracting_bibtex.py)
	- script just extracts bibtex from the ORCID
* [orcid_bibtex_to_html.py](orcid_bibtex_to_html.py)
	- iterates through the list or ID's, extracts ORCID, creates bat file to compile bibtex into HTMLs with help of JabRef
		+ List should be in the python dict format, here is the example (I created file 'vlbalist.py')
		```
		orcid_list = {
			'John Wilbanks' : '0000-0002-4510-0385',
			}

		```
        + To make in run on Mac OS, it's better if you will copy JabRef into the 'generated' folder directly
* [search_authors.py](search_authors.py)
	- various ways to perform searches (e.g. author name)
