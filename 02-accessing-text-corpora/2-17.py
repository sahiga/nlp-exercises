#!/usr/bin/env python

import nltk
from nltk.corpus import stopwords

# Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.

def common_words(text, language, num_words):
    fdist = nltk.FreqDist([w.lower() for w in text])
    words = [' '] * num_words
    n = 0
    
    while n < len(words):
        for key in fdist.keys():
            if key not in nltk.corpus.stopwords.words(language):
                words[n] = key
                n = n + 1
            else:
                n = n

    return words

def cw(text, language, num_words):
    fdist = nltk.FreqDist([w.lower() for w in text])
    words = []

    for key in fdist.keys():
        if key not in nltk.corpus.stopwords.words(language):
            words.append(key)

    return words[:num_words]
