import spacy
import random
from spacy.util import minibatch, compounding
from spacy.language import Language
from spacy.tokens import Doc, Token, Span

model_name = 'C:\Proyectos\AnalisiLogica\it_model_mons'


class NLPCustomRules(object):
    Token.set_extension("is_name", default=False)

    def new_component(doc):

        #print("After tokenization, this doc has {} tokens.".format(len(doc)))
        #print("The part-of-speech tags are:", [token.pos_ for token in doc])

        for token in doc:
            if token.text == 'Formatisi':
                token._.is_name = ' Formare'

        #if len(doc) < 10:
            #print("This is a pretty short document.")

        return doc

#Model factories
Language.factories['parser1'] = lambda nlp, **cfg: NLPCustomRules.new_component(nlp, **cfg)

nlp = spacy.load('it_core_news_sm')

nlp.add_pipe(NLPCustomRules.new_component, name='parser1', last=True)

# Parser training data
TRAIN_DATA = [
    (
        "gioca in cucina",
        {
            "heads": [0, 2, 0],
            "deps": ["ROOT", "PLACE", "ROOT"],
        },
    ),
    (
        "corre nel salone",
        {
            "heads": [0, 2, 0],
            "deps": ["ROOT", "PLACE", "ROOT"],
        },
    )

]


#nlp = spacy.load("it_core_news_sm")

# We'll use the built-in dependency parser class, but we want to create a
# fresh instance – just in case.
if "parser1" in nlp.pipe_names:
    nlp.remove_pipe("parser1")

parser1 = nlp.create_pipe("parser1")
nlp.add_pipe(parser1, first=True)

for text, annotations in TRAIN_DATA:
    for dep in annotations.get("deps", []):
        parser1.add_label(dep)

pipe_exceptions = ["parser1", "trf_wordpiecer", "trf_tok2vec"]
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

n_iter = 7

with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        # batch up the examples using spaCy's minibatch
        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            texts, annotations = zip(*batch)
            nlp.update(texts, annotations, sgd=optimizer, losses=losses)
        print("Losses", losses)


#Save the model
nlp.to_disk(model_name)


nlp = spacy.load(model_name)

doc = nlp("Il vento scuote i rami degli alberi.")

print(nlp.pipeline)

print([(t.text, t.dep_, t.head.text) for t in doc if t.dep_ != "-"])







textcat = nlp.get_pipe("my_component11")
#nlp.disable_pipes("my_component")


for text, annotations in TRAIN_DATA:
  for dep in annotations.get("deps", []):
    textcat.add_label(dep)


pipe_exceptions = ["textcat"]
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

n_iter = 7

with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        # batch up the examples using spaCy's minibatch
        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            texts, annotations = zip(*batch)
            nlp.update(texts, annotations, sgd=optimizer, losses=losses)
        print("Losses", losses)


def my_component(doc):
  print("After tokenization, this doc has {} tokens.".format(len(doc)))
  print("The part-of-speech tags are:", [token.pos_ for token in doc])

  Token.set_extension('is_name', default=False)

  for token in doc:
    if token.text == 'Formatisi':
      token._.is_name = ' Formare'

  if len(doc) < 10:
    print("This is a pretty short document.")
  return doc


TRAIN_DATA = [
    (
        "gioca in cucina",
        {
            "heads": [0, 2, 0],
            "deps": ["ROOT", "PLACE", "ROOT"],
        },
    ),
    (
        "corre nel salone",
        {
            "heads": [0, 2, 0],
            "deps": ["ROOT", "PLACE", "ROOT"],
        },
    )

]
