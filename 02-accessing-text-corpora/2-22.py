#!/usr/bin/env python

# Define a function hedge(text) which processes a text and produces a new version with the word 'like' between every third word.

def hedge(text):
    n = 3
    like = list(text)

    while n <= len(like):
        like.insert(n, 'like')
        n = n + 4

    for w in like:
        print w,
