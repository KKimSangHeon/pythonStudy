import nltk
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

print(tokenizer)

from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords

def tokenizer_twit(doc):
    return ['/'.join(t) for t in twi_tagger.pos(doc, norm=True, stem=True)]