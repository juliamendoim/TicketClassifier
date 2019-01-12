from collections import defaultdict

from nltk.corpus import stopwords
import spacy


nlp = spacy.load('de')

stopWords = set(stopwords.words('german'))

with open('corpus/unclustered_input.txt', 'r', encoding='utf-8') as f:
    raw = f.readlines()

# create a spacy object

corpus = [nlp(utterance) for utterance in raw]  # spacy object

# lematize, remove stopwords and punctuation

lemmas = ' '.join([y.lemma_ for x in corpus for y in x if y.is_stop is False and y.lemma_.lower() not in stopWords] )

# save clean corpus

with open('clean/lemmas_corpus.txt', 'w', encoding='utf-8') as f:
    f.write(lemmas)

# tokens and vocabulary

original_tokens = [y.text for x in corpus for y in x]
tokens = [y.lemma_ for x in corpus for y in x if y.is_stop is False and y.lemma_.lower() not in stopWords]

print('There where ' + str(len(original_tokens)) + ' tokens in original corpus')
print('There are ' + str(len(tokens)) + ' tokens in clean corpus')

original_vocabulary = set(original_tokens)
vocabulary = set(tokens)

print('There where ' + str(len(original_vocabulary)) + ' unique words in original corpus')
print('There are ' + str(len(vocabulary)) + ' unique lemmas in clean corpus')

# frequency dict

frequency_dict = defaultdict(int)

for token in tokens:
    frequency_dict[token] += 1

print('Frecuency dictionary ', frequency_dict)
