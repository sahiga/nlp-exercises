#!/usr/bin/env python

import nltk
from nltk.corpus import brown

# Write a program to create a table of word frequencies by genre, like the one given in _sec-extracting-text-from-corpora for modals. Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings.

def word_frequencies(text, words):
    cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in text.categories()
        for word in text.words(categories=genre))

    return cfd.tabulate(samples=words)
