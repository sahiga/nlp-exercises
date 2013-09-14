#!/usr/bin/env python

import nltk, random

# Modify the text generation program in 2.5 further, to do the following tasks:

# Store the n most likely words in a list words then randomly choose a word from the list using random.choice(). (You will need to import random first.)

# Select a particular genre, such as a section of the Brown Corpus, or a genesis translation, one of the Gutenberg texts, or one of the Web texts. Train the model on this corpus and get it to generate random text. You may have to experiment with different start words.

def generate_model_random(cfdist, word, num):
    i = 0

    for i in range(num):
        print word,
        words = cfdist[word].keys()[:num]
        word = random.choice(words)
