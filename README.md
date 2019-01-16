# TicketClassifier

An unsupervised model for text classification of short sentences 

## Getting Started

pip install -r **requirements.txt**

for the spacy_model:

- python -m spacy download de

for the nltk_stopwords, from a python console:

- import nltk
- nltk.download('stopwords')


### Prerequisites

- Python3.6


### Running

- python clustering.py *spacy_model* *nltk_stopwords* *n_clusters* *raw_input* 

or help:

- python clustering.py -h 


## Built With

* [Spacy](https://spacy.io/models/) - Spacy
* [Sklearn](https://scikit-learn.org/stable/modules/clustering.html#clustering) - sklearn.cluster

## Authors

* **Julia Milanese** - [Julia Milanese](https://github.com/juliamendoim)

