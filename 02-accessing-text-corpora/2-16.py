#!/usr/bin/env python

import nltk
from nltk.corpus import brown

# Write a program to generate a table of lexical diversity scores (i.e. token/type ratios), as we saw in 1.1. Include the full set of Brown Corpus genres (nltk.corpus.brown.categories()). Which genre has the lowest diversity (greatest number of tokens per type)? Is this what you would have expected?

def lexical_diversity_table(corpus):
    ld = [' ']
    for genre in corpus.categories():
              ld.append(len(corpus.words(categories=genre))/len(set(corpus.words(categories=genre))))

    cfd = nltk.ConditionalFreqDist(
        (genre_name, genre_count)
        for genre_name in corpus.categories()
        for genre_count in ld)

    return cfd.plot()

def ldt(corpus):
    cfd = nltk.ConditionalFreqDist(
        (genre, len(corpus.words(categories=genre))/len(set(corpus.words(categories=genre))))
        for genre in corpus.categories()
        )

    return cfd.tabulate()

def ld(corpus):
    for genre in corpus.categories():
        ld = len(corpus.words(categories=genre))/len(set(corpus.words(categories=genre)))
        print genre + ':', ld
    return 0
