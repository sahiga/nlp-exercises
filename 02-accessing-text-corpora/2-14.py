#!/usr/bin/env python

import nltk
from nltk.corpus import wordnet as wn

# Define a function supergloss(s) that takes a synset s as its argument and returns a string consisting of the concatenation of the definition of s, and the definitions of all the hypernyms and hyponyms of s.

def supergloss(s):
    n = 0
    synset = (s.name, s.definition)
    hypernyms = s.hypernyms()
    hyponyms = s.hyponyms()

    if hypernyms != []:
        while n < len(hypernyms):
            for hypernym in s.hypernyms():
                hypernyms[n] = (hypernym.name, hypernym.definition)
                n = n + 1
    else:
        hypernyms = 'none'

    n = 0
    if hyponyms != []:
        while n < len(hyponyms):
            for hyponym in hyponyms:
                hyponyms[n] = (hyponym.name, hyponym.definition)
                n = n + 1
    else:
        hyponyms = 'none'

    total = 'ROOT WORD:', synset, 'HYPERNYMS:', hypernyms, 'HYPONYMS:', hyponyms
    return total
