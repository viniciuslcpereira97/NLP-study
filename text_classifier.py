##!usr/bin/env python
#-*- coding: utf-8 -*-
#

from nltk.corpus import floresta
from nltk.corpus import mac_morpho
from nltk import NaiveBayesClassifier
import matplotlib.pyplot as plt

train_set = []
supervisioned_labels =  floresta.tagged_sents()

for sentence in supervisioned_labels:
    for item in sentence:
        train_set.append( ({'word': item[0]}, item[1]) )

classifier = NaiveBayesClassifier.train( train_set )

phrase = "crie os gráficos para os dispositivos android desde novembro".split()
tagged_input = [ ( classifier.classify( {'word': x} ), x ) for x in phrase ]
tagged_tree = { key[0]: [ value[1] if value[0] == key[0] else None for value in tagged_input ]  for key in tagged_input }

for item in tagged_tree:
    tagged_tree[item] = filter( lambda x: x != None ,tagged_tree[item] )

print tagged_tree