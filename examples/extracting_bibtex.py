# coding: utf-8

# importing module located in parent folder
import sys
sys.path.insert(0, '../')

# maing testing library
import pyorcid as orcid

# additional libraries
import os
import json
import codecs

# setting logging to the DEBUG mode
import logging

#logging.getLogger("#orcid#").setLevel(logging.DEBUG)
logging.getLogger("#orcid#").setLevel(logging.INFO)

#retrieve my own's profile from his ORCID
me = orcid.get('0000-0001-5661-4587')

TARGET_FODLER = 'generated'

def print_keyword(obj):
    """ Printing author keywords """

    print('[i] printing author keywords')
    for key_word in obj.keywords:
        print (key_word)

def print_publications(obj):
    """ Printing author publications """

    print('[i] printing author publications')
    for value in obj.publications:
        print (value)

def save_bibtex(bibtex, file_name='orcid-bibtex-output.bib', encoding='utf-8'):
    """
        (dict, str, str) -> None

        Saving bibtex to the file, grouped by year.
    """

    file_name = '{0}/{1}'.format(TARGET_FODLER, file_name)

    _file = codecs.open(file_name, 'w', encoding)

    for key in bibtex:
        _file.write("%%%%%%%%%%%%%%%% \n%% %s \n%%%%%%%%%%%%%%%%\n\n" % key)
        bibtex_group = ''
        for value in bibtex[key]:
            bibtex_group += value + '\n\n'
        _file.write(bibtex_group)

    _file.close()

    print('[i] bibtex was created, check following file: {0}'.format(file_name))

def save_nocite(bibtex, file_name='orcid-nocite-output.tex', encoding='utf-8'):
    """
        (dict, str, str) -> None

        Saving bibtex to the file, grouped by year.
    """

    def extract_bibtex_id(s):
        start = s.find('{') + 1
        end = s.find(',', start)
        return  s[start:end]

    file_name = '{0}/{1}'.format(TARGET_FODLER, file_name)

    _file = codecs.open(file_name, 'w', encoding)

    for key in bibtex:
        _file.write("%%%%%%%%%%%%%%%% \n%% %s \n%%%%%%%%%%%%%%%%\n\n" % key)
        nocite_group = ''
        for value in bibtex[key]:
            nocite_group += '\\nocite{' + extract_bibtex_id(value) + '}' + '\n'
        _file.write(nocite_group)

    _file.close()

    print('[i] tex with \\nocite was created, check following file: {0}'.format(file_name))

def extract_bitex(obj):
    """
        (Class) -> dict()

        Method takes as an input object with all publications from ORCID and forms dict with it.
    """

    bibtex = {}
    for value in obj.publications:
        if value.citation_type == 'BIBTEX':
            if value.publicationyear not in bibtex:
                bibtex[value.publicationyear] = list()
                bibtex[value.publicationyear].append(value.citation_value)
            else:
                bibtex[value.publicationyear].append(value.citation_value)
        else:
            print ('[i] this publications is having no BIBTEX {0}'.format(value))

    return bibtex

def orcid_bibtex(obj):
    """
        (Class) -> None

        Extrating bibtex from ORCID, saving it to the file
    """

    if not os.path.exists(TARGET_FODLER):
        os.makedirs(TARGET_FODLER)

    # extracting bibtex
    orcid_bibtex = extract_bitex(me)

    # saving bibtex to file
    save_bibtex(orcid_bibtex)

    # citing extracted bibtex
    save_nocite(orcid_bibtex)

#print_keyword(me)
#print_publications(me)
orcid_bibtex(me)
