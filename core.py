#!usr/bin/env python
#-*- coding: utf-8 -*-

import random
import nltk
from nltk import NaiveBayesClassifier
from nltk.corpus import names
import matplotlib.pyplot as plt

male_names = open("/home/diego/Downloads/Telegram Desktop/nomes_masculinos").read().split('\n')
female_names = open("/home/diego/Downloads/Telegram Desktop/nomes_femininos").read().split('\n')

def gender_features(word):
    return {'last_letter': word[-1]}

labeled_names = ([(name, 'male') for name in male_names] + [(name, 'female') for name in female_names])
# random.shuffle(labeled_names)

features_sets = [( gender_features(name), gender ) for (name, gender) in labeled_names]

train_set, test_set = features_sets, features_sets[:500]

print train_set[0]

classifier = NaiveBayesClassifier.train( train_set )

print classifier.classify( gender_features("vinicius") )

plt.scatter(  )
plt.show()
# print nltk.classify.accuracy( classifier, test_set )
