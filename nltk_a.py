
import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn

ita_stemmer = nltk.stem.snowball.ItalianStemmer()


text = "L'amore è nell'aria"

print(sorted(wn.langs()))

cane_lemmas = wn.lemmas("cane", lang="ita")

print(cane_lemmas)

#Tokenize the text
tex = word_tokenize(text)

for token in tex:
    print(nltk.pos_tag([token]))