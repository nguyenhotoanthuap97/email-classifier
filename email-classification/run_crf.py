from bs4 import BeautifulSoup as bs
from bs4.element import Tag
import codecs
import nltk
from nltk import word_tokenize, pos_tag
from nltk.tag.crf import CRFTagger
from sklearn.model_selection import train_test_split
import pycrfsuite
import os, os.path, sys
import glob
from xml.etree import ElementTree
import numpy as np
from sklearn.metrics import classification_report
import pandas as pd

# datasets = pd.read_csv('../datasets/emails.csv')
# X_train = datasets.iloc[0:5169, 1:3002].values
# Y_train = datasets.iloc[0:5169, 3001].values
# X_test = datasets.iloc[5169:5172, 1:3001].values

# crf_model = CRFTagger()
# crf_model.train(X_train, 'crf.model')
# crf_model.tag_sents(X_test)
nltk.download('conll2002')
train_sents = list(nltk.corpus.conll2002.iob_sents('esp.train'))

print(train_sents[0])