#!/usr/bin/env python

import nltk
from nltk.corpus import udhr

# Define a function find_language() that takes a string as its argument, and returns a list of languages that have that string as a word. Use the udhr corpus and limit your searches to files in the Latin-1 encoding.

def find_language(string):
    languages = []
    target_languages = []

    for name in nltk.corpus.udhr.fileids():
        if 'Latin1' in name:
            languages.append(name)

    for lang in languages:
        if string in nltk.corpus.udhr.words(lang):
            target_languages.append(lang)

    return target_languages
