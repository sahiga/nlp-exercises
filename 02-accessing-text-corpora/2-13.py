#!/usr/bin/env python

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

# What percentage of noun synsets have no hyponyms? You can get all noun synsets using wn.all_synsets('n').

def synset_percentage(synset_group, lexical_relation):
    n = 0
    group = list(synset_group) # copies generator synset_group into a list
    total_length = len(group)
    lexical = list(group)
    lexical_length = len(lexical)
    while n < 0:
        for synset in synset_group:
            if synset.lexical_relation == []:
                lexical[n] = synset
                n = n + 1
            else:
                n = n
    return lexical_length / total_length * 100
