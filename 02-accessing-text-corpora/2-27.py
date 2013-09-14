#!/usr/bin/env python

from __future__ import division
import nltk
from nltk.corpus import wordnet as wn

# The polysemy of a word is the number of senses it has. Using WordNet, we can determine that the noun dog has 7 senses with: len(wn.synsets('dog', 'n')). Compute the average polysemy of nouns, verbs, adjectives and adverbs according to WordNet.

def polysemy(group):
    polysemy = 0
    count = 0
    name = ''

    for synset in wn.all_synsets(group):
        for lemma in synset.lemmas:
            name = lemma.name
            polysemy = polysemy + len(wn.synsets(name, group))
            count = count + 1

    return polysemy / count

# nouns = 'n': 1.852...
# verbs = 'v': 5.098...
# adverbs = 'r': 1.698...
# adjectives = 'a': 2.233...
