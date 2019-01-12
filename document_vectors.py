import spacy

nlp = spacy.load('de')

# spacy document vectors

with open('clean/lemmas_corpus.txt', 'r', encoding='utf-8') as f:
    corpus_vectores = f.readlines()

doc = [nlp(sentence) for sentence in corpus_vectores]

document_vectors = [x.vector for x in doc]
