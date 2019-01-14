#  -*- coding: utf-8 -*-


def preprocessor(text, nlp, stopWords):

    corpus = [nlp(utterance) for utterance in text]

    lemmas = [y.lemma_ for x in corpus for y in x if y.is_stop is False and y.is_punct is False and y.lemma_.lower() not in stopWords]
    lematized_text = ' '.join(lemmas).split('\n')
    print(lematized_text)

    original_tokens = [y.text for x in corpus for y in x]

    print('There where ' + str(len(original_tokens)) + ' tokens in original corpus')
    print('There are ' + str(len(lemmas)) + ' tokens in clean corpus')

    original_vocabulary = set(original_tokens)
    vocabulary = set(lemmas)

    print('There where ' + str(len(original_vocabulary)) + ' unique words in original corpus')
    print('There are ' + str(len(vocabulary)) + ' unique lemmas in clean corpus')

    # frequency dict

    from collections import defaultdict

    frequency_dict = defaultdict(int)

    for token in lemmas:
        frequency_dict[token] += 1

    print('Frecuency dictionary ', frequency_dict)

    return lematized_text
