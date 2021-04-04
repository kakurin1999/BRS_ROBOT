# install spacy command
# pip install -U pip setuptools wheel
# pip install -U spacy
# python -m spacy download ru_core_news_lg

import spacy
nlp = spacy.load("ru_core_news_lg")
doc = nlp("No text available yet")
print([(w.text, w.pos_) for w in doc])