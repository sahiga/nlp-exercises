#!/usr/bin/env python

import nltk, pylab, matplotlib, random

# Zipf's Law: Let f(w) be the frequency of a word w in free text. Suppose that all the words of a text are ranked according to their frequency, with the most frequent word first. Zipf's law states that the frequency of a word type is inversely proportional to its rank (i.e. f × r = k, for some constant k). For example, the 50th most common word type should occur three times as frequently as the 150th most common word type.

# Write a function to process a large text and plot word frequency against word rank using pylab.plot. Do you confirm Zipf's law? (Hint: it helps to use a logarithmic scale). What is going on at the extreme ends of the plotted line?

# Generate random text, e.g., using random.choice("abcdefg "), taking care to include the space character. You will need to import random first. Use the string concatenation operator to accumulate characters into a (very) long string. Then tokenize this string, and generate the Zipf plot as before, and compare the two plots. What do you make of Zipf's Law in the light of this?

def freq_rank(text):
    fdist = nltk.FreqDist([w.lower() for w in text])
    keys = fdist.keys()
    freq = []
    rank = []
    n = 1 # must start at 1 because log10(0) = infinity

    for w in keys:
        frequency = Decimal.logb(Decimal(fdist[w]))
        freq.append(frequency)

    for w in keys:
        rank.append(Decimal.logb(Decimal(n)))
        n = n + 1

    pylab.plot(rank, freq)
    return pylab.show()

def freq_rank_scramble(text):
    n = 0
    scrambled = ''
    freq = []
    rank = []

    while n < len(text):
        scrambled = scrambled + ' ' + random.choice(text)
        n = n + 1

    scrambled = scrambled.split()

    fdist = nltk.FreqDist([w.lower() for w in scrambled])
    keys = fdist.keys()

    n = 1
    for w in keys:
        frequency = Decimal.logb(Decimal(fdist[w]))
        freq.append(frequency)
        rank.append(Decimal.logb(Decimal(n)))
        n = n + 1
    
    pylab.plot(rank, freq)
    return pylab.show()
