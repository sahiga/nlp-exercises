#!/usr/bin/env python

import nltk
from nltk.corpus import brown

# Write a program to find all words that occur at least three times in the Brown Corpus.

def many_words(corpus, number):
    fdist = nltk.FreqDist([w.lower() for w in corpus])
    words = [' ']
    for word in fdist:
        if fdist[word] >= number:
            words.append(word)
    return words
