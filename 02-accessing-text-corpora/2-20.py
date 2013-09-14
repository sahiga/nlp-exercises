#!/usr/bin/env python

import nltk
from nltk.corpus import brown

# Write a function word_freq() that takes a word and the name of a section of the Brown Corpus as arguments, and computes the frequency of the word in that section of the corpus.

def word_freq(word, genre):
    fdist = nltk.FreqDist([w.lower() for w in nltk.corpus.brown.words(categories=genre)])
    return fdist[word]
