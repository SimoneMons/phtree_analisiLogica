import spacy
from spacy.util import minibatch, compounding

nlp = spacy.blank("en")  # create blank Language class

print("Created blank 'en' model")