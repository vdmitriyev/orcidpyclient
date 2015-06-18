# coding: utf-8

# importing module located in parent folder
import sys
sys.path.insert(0, '../')

# maing testing library
import pyorcid as orcid

# additional libraries
import os
import json
import uuid
import codecs

# setting logging to the DEBUG mode
import logging

#logging.getLogger("orcid-bibtex-to-html").setLevel(logging.DEBUG)
logging.getLogger("orcid-bibtex-to-html").setLevel(logging.INFO)

TARGET_FODLER = 'generated'

UMLAUT_TO_LATEX = {
    u'Ö' : '\\"{O}',
    u'ö' : '\\"{o}',
    u'ä' : '\\"{a}',
    u'Ä' : '\\"{A}',
    u'Ü' : '\\"{U}',
    u'ü' : '\\"{u}',
    u'ß' : '{\\ss}'
}

def generate_bat(orcid_list, bat_name = 'build-all.bat', encoding='utf-8'):
    """
        (list, str, str) -> None

        Generating command bat file
    """

    cmd_header = 'REM SETTING PATH to JabRef\n'
    cmd_header += 'set PATH=%PATH%;c:\\Soft\\JabRef\\; \n\n'

    #template = 'java -jar JabRef-2.10.jar -o "{0}".html,htmlvlba -n true "{0}".bib\n'
    template = 'JabRef-2.10.jar -o "{0}".html,htmlvlba -n true "{0}".bib\n'

    cmd = ''
    for key in orcid_list:
        cmd += template.format(key)

    file_name = '{0}/{1}'.format(TARGET_FODLER, bat_name)
    _file = codecs.open(file_name, 'w', encoding)
    _file.write(cmd_header)
    _file.write(cmd)
    _file.close()


def save_bibtex(bibtex, file_prefix='orcid-bibtex-output', separate=False, encoding='utf-8'):
    """
        (dict, str, str) -> None

        - saving bibtex to the files, if required separating by year.
    """

    file_name = '{0}/{1}'.format(TARGET_FODLER, file_prefix)

    if not separate:
        _file = codecs.open(file_name + '.bib', 'w', encoding)

    for key in bibtex:

        if separate:
            _file = codecs.open(file_name + '-' + str(key) + '.bib', 'w', encoding)

        _file.write("%%%%%%%%%%%%%%%% \n%% %s \n%%%%%%%%%%%%%%%%\n\n" % key)

        bibtex_group = ''
        for value in bibtex[key]:
            bibtex_group += value + '\n\n'
        _file.write(bibtex_group)

        if separate:
            _file.close()

    if not separate:
        _file.close()


    print '[i] bibtex was created, check following file: %s ' % (file_name)

def form_bibtex(authors, title, year):
    """
        - forming bibtex
    """

    template = '@InProceedings{0}{2} , \n\t Title = {0}{3}{1}, \n\t Author = {0}{4}{1}, \n\t Year = {0}{5}{1}\n{1}'
    _authors = ' and '.join(authors)
    try:
        _title = title
        for x in UMLAUT_TO_LATEX:
            _title = _title.replace(x, UMLAUT_TO_LATEX[x])
    except Exception as ex:
        _title = title

    return template.format('{','}', str(uuid.uuid1())[:13], _title, _authors, year)

def extract_bitex(obj, author):
    """
        (Class) -> dict()

        Method takes as an input object with all publications from ORCID and forms dict with it.
    """

    bibtex = {}
    nobibtex = list()

    for value in obj.publications:
        try:
            if value.citation.citation_type == 'BIBTEX':
                if value.publicationyear not in bibtex:
                    bibtex[value.publicationyear] = list()
                    bibtex[value.publicationyear].append(value.citation.citation)
                else:
                    bibtex[value.publicationyear].append(value.citation.citation)
            else:
                # nobibtex.append('% ' + value.title)
                nobibtex.append(form_bibtex([author], value.title, value.publicationyear))
                print '[i] this publications is having no BIBTEX, new BIBTEX was generated {0}'.format(value.title)
        except Exception as ex:
            print '[e] exception: {0}'.format(str(ex))
            # print '[i] following publication was not added: {0}'.format(value.title)
            print '[i] new BIBTEX was generated {0}'.format(value.title)
            # nobibtex.append('% ' + value.title)
            nobibtex.append(form_bibtex([author], value.title, value.publicationyear))

    if nobibtex:
        bibtex['nobibtex'] = nobibtex

    return bibtex

def main():
    """
        (list) -> None

        Extrating bibtex from ORCID, saving it to the file
    """

    import vlbalist as ol
    orcid_list = ol.orcid_list

    orcid_extracted = list()

    if not os.path.exists(TARGET_FODLER):
        os.makedirs(TARGET_FODLER)

    # extracting bibtex
    for key in orcid_list:

        name = key
        orcidid = orcid_list[key]
        print '[i] extracting bibtex for {0}'.format(name)
        orcid_obj = orcid.get(orcidid)

        # extracting bibtex
        try:
            orcid_bibtex = extract_bitex(orcid_obj, author = name)

            # saving bibtex into separated files
            save_bibtex(bibtex=orcid_bibtex, file_prefix=name, separate=False)
            orcid_extracted.append(name)
        except Exception as ex:
            print '[i] exception happened'
            print '[e] exception: {0}'.format(str(ex))

    generate_bat(orcid_extracted)

if __name__ == '__main__':

    # setting system default encoding to the UTF-8
    reload(sys)
    sys.setdefaultencoding('UTF8')

    # initiating main processing
    main()
