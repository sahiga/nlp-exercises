#!/usr/bin/env python

import nltk
from nltk.corpus import stopwords

# Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.

def cw_bigrams(text, language, num_bigrams):
    
    bigrams = nltk.bigrams([w.lower() for w in text])

    fdist = nltk.FreqDist(bigrams)
    keys = fdist.keys()
    stopwords = nltk.corpus.stopwords.words(language)
    clean = []

    for bigram in keys:
        if bigram[0] not in stopwords:
            if bigram[1] not in stopwords:
                clean.append(bigram)

    return clean[:num_bigrams]
