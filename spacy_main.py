# install spacy command
# pip install -U pip setuptools wheel
# pip install -U spacy
# python -m spacy download ru_core_news_lg
from dataEMail import *
import spacy
import os
from spacy import displacy
from IPython.core.display import display, HTML
from IPython.display import IFrame

def extended_is_stop(token):
    stop_words = nlp.Defaults.stop_words
    return token.is_stop or token.lower_ in stop_words or token.lemma_ in stop_words

nlp = spacy.load("ru_core_news_lg")

path = "email/sfedu"
list_files = sorted(os.listdir(path))
mess = getMess(path + '/' + list_files[1])
print(mess)

doc = nlp(mess)
print([(w.text, w.pos_, extended_is_stop(w)) for w in doc])

html = displacy.serve(doc, style="dep")







