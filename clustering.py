#  -*- coding: utf-8 -*-

import sys
import argparse

from preprocessing import preprocessor

from nltk.corpus import stopwords
import spacy

import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer

parser = argparse.ArgumentParser(description='Clustering')
parser.add_argument('*spacy_model', type=str, help='Language: de')
parser.add_argument('*nltk_stopwords', type=str, help='Stopwords: german')
parser.add_argument('*n_clusters', type=int, help='Number of clusters')
parser.add_argument('*input_file', type=str, help='input raw file with \\n sentence separation')

args = parser.parse_args()

if not args:
    parser.print_usage()
    sys.exit(1)

nlp = spacy.load(args.spacy_model)

stopWords = set(stopwords.words(args.nltk_stopwords))

raw_text = args.input_file

with open(raw_text, 'r', encoding='utf-8') as f:
    text = f.readlines()

clean_corpus = preprocessor(text, nlp, stopWords)


tfidfvect = TfidfVectorizer()
agglomerative = AgglomerativeClustering(n_clusters=args.n_clusters, affinity='euclidean', linkage='ward')

tfidfmatrix = tfidfvect.fit_transform(clean_corpus)

aggclusters = agglomerative.fit(tfidfmatrix.toarray())

print(pd.DataFrame(aggclusters.labels_, clean_corpus))
