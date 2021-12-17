# NLP-Basics

#### Author: Dwayne Fernandes. 
You can reach me out at dwayne.ferns16@gmail.com

The repository has two NLP techniques:-

### 1) Parts-Of-Speech(POS) Tagging:

<p align="center">
  <img width="800" height="300" src="https://d33wubrfki0l68.cloudfront.net/d5cbc4b0e14c20f877366b69b9171649afe11fda/d96a8/assets/images/bigram-hmm/pos-title.jpg">
</p>

In corpus linguistics, part-of-speech tagging (POS tagging or PoS tagging or POST), also called grammatical tagging is the process of marking up a word in a text (corpus) as corresponding to a particular part of speech,[1] based on both its definition and its context. A simplified form of this is commonly taught to school-age children, in the identification of words as nouns, verbs, adjectives, adverbs, etc.

**Datasets:** Used the news articles provided by the Brown, and Reuters Corpus by the NLTK library.

I trained a **Unigram POS Tagger** provided by the NLTK library to train on the Brown news corpus.

**Accuracy:** Testing accuracy achieved was 88% on the Brow-test data.

### 2) Multi-class classification of Text Data:

<p align="center">
  <img width="800" height="300" src="https://miro.medium.com/max/1000/1*HgXA9v1EsqlrRDaC_iORhQ.png">
</p>

One of the widely used natural language processing task in different business problems is “Text Classification”. The goal of text classification is to automatically classify the text documents into one or more defined categories. Some examples of text classification are:

* Understanding audience sentiment from social media,
* Detection of spam and non-spam emails,
* Auto tagging of customer queries, and
* Categorization of news articles into defined topics.

The multi-class classifier is able to classify a given news article into any of the following 5 categories **('business', 'tech', 'politics', 'sport', 'entertainment').**


**Dataset:** BBC News Dataset.

**Feature Extraction Technique:**Tfidf-Vectorizer.

TF-IDF are word frequency scores that try to highlight words that are more interesting, e.g. frequent in a document but not across documents. The TfidfVectorizer will tokenize documents, learn the vocabulary and inverse document frequency weightings, and allow you to encode new documents.

**Algorithm:** Random Forest.

Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operate by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees. Random decision forests correct for decision trees' habit of overfitting to their training set.

**Precision & F1 score:** 97%.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python package manager.
```bash
pip install nltk
pip install pandas
pip install sklearn
```

## Usage

```POS_tagger.ipynb```: This notebook has the code to the POS tagger.


```news_classifier.ipynb```: This notebook has the code to the Multi-class News Classification.

```BBC News Train.csv```: This is the dataset used for Multi-class classfication.
