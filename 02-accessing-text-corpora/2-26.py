#!/usr/bin/env python

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

# What is the branching factor of the noun hypernym hierarchy? I.e. for every noun synset that has hyponyms — or children in the hypernym hierarchy — how many do they have on average? You can get all noun synsets using wn.all_synsets('n').

def branching_factor(synset_group, lexical_relation):
    total = 0
    count = 0

    for synset in synset_group:
        if synset.lexical_relation != []:
            total = total + len(synset.lexical_relation)
            count = count + 1

    return total / count
