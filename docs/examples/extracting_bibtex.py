import codecs
import logging
import os

try:
    import orcidpyclient
except:

    import os
    import sys
    from pathlib import Path

    current_path = Path(os.path.abspath(os.path.dirname(__file__)))
    _path_to_add = os.path.join(str(current_path.parent.parent))
    print(f"[i] Try following path to load package: {_path_to_add})")
    sys.path.append(_path_to_add)

    import orcidpyclient

    print(f"[i] Use dev version of package with version")


logging.getLogger(__name__).setLevel(logging.INFO)

TARGET_FODLER = "generated"
ORCID_ID = "0000-0001-5661-4587"


def save_bibtex(bibtex, file_name="orcid-bibtex-output.bib", encoding="utf-8"):
    """
    (dict, str, str) -> None

    Saves BibTeX into the file, grouping them by year.
    """

    file_name = "{0}/{1}".format(TARGET_FODLER, file_name)

    _file = codecs.open(file_name, "w", encoding)

    for key in bibtex:
        _file.write("%%%%%%%%%%%%%%%% \n%% %s \n%%%%%%%%%%%%%%%%\n\n" % key)
        bibtex_group = ""
        for value in bibtex[key]:
            bibtex_group += value + "\n\n"
        _file.write(bibtex_group)

    _file.close()

    print("[i] bibtex was created, check following file: {0}".format(file_name))


def save_nocite(bibtex, file_name="orcid-nocite-output.tex", encoding="utf-8"):
    """
    (dict, str, str) -> None

    Saves BibTeX to the file with "nocite" command, grouped by year.
    """

    def extract_bibtex_id(s):
        start = s.find("{") + 1
        end = s.find(",", start)
        return s[start:end]

    file_name = "{0}/{1}".format(TARGET_FODLER, file_name)

    _file = codecs.open(file_name, "w", encoding)

    for key in bibtex:
        _file.write("%%%%%%%%%%%%%%%% \n%% %s \n%%%%%%%%%%%%%%%%\n\n" % key)
        nocite_group = ""
        for value in bibtex[key]:
            nocite_group += "\\nocite{" + extract_bibtex_id(value) + "}" + "\n"
        _file.write(nocite_group)

    _file.close()

    print(
        "[i] tex with \\nocite was created, check following file: {0}".format(file_name)
    )


def extract_bibtex(obj):
    """
    (Class) -> dict()

    Takes an object with all publications from ORCID as the input and forms dict out of it.
    """

    bibtex = {}
    for value in obj.publications:
        if value.citation_type.lower() == "bibtex":
            if value.publicationyear not in bibtex:
                bibtex[value.publicationyear] = list()
                bibtex[value.publicationyear].append(value.citation_value)
            else:
                bibtex[value.publicationyear].append(value.citation_value)
        else:
            print("[i] this publications is having NO BibTeX {0}".format(value))

    return bibtex


def extract_bibtex_orcid(orcid_profile):
    """
    (Class) -> None

    Extracts BibTeX from ORCID, saves it into the file
    """

    if not os.path.exists(TARGET_FODLER):
        os.makedirs(TARGET_FODLER)

    # extracting bibtex
    orcid_bibtex = extract_bibtex(orcid_profile)

    # saving bibtex to file
    save_bibtex(orcid_bibtex)

    # citing extracted bibtex
    save_nocite(orcid_bibtex)


if __name__ == "__main__":
    # retrieve a profile from his ORCID
    orcid_profile = orcidpyclient.get(ORCID_ID, debug=False)
    extract_bibtex_orcid(orcid_profile)
