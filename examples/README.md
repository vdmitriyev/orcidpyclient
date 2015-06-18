### About

'Ready to run' examples showing how to use **orcid** python module.

### How to run examples
* To run the examples no installation of **orcid** module is required.
* Download latest package from [github](https://github.com/scholrly/orcid-python) and unzip it
* Install dependencies (see file 'requirements.txt')
* Navigate to the subfolder 'examples'
* For instance, to run **extracting_bibtex.py** use following command:
```
python extracting_bibtex.py
```

### Examples

* [extracting_bibtex.py](extracting_bibtex.py)
	- script just extracts bibtex from the Orcid
* [orcid_bibtex_to_html.py](orcid_bibtex_to_html.py)
	- iterates through the list or ID's, extracts orcid, creates bat file to compile bibtex into HTMLs with help of JabRef
		+ List should be in the python dict format, here is the example (I created file 'vlbalist.py')
		```
		orcid_list = {
			'Viktor Dmitriyev' : '0000-0001-5661-4587',
			}

		```
        + To make in run on Mac OS, it's better if you will copy JabRef into the 'generated' folder directly
