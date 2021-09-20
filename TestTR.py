import spacy
import random
from spacy.util import minibatch, compounding

model_name = 'C:\Proyectos\AnalisiLogica\it_model_mons'

# Parser training data
TRAIN_DATA = [
    (
        "Il gatto di Chiara gioca in cucina",
        {
            "heads": [0, 0, 0, 0, 4, 6, 4],
            "deps": ["-", "-", "-", "-", "ROOT", "-", "PLACE"],
        },
    ),
    (
        "Il cane di Lucia corre nel salone",
        {
            "heads": [0, 0, 0, 0, 4, 6, 4],
            "deps": ["-", "-", "-", "-", "ROOT", "-", "PLACE"],
        },
    )

]


nlp = spacy.load("it_core_news_sm")

# We'll use the built-in dependency parser class, but we want to create a
# fresh instance – just in case.
if "parser" in nlp.pipe_names:
    nlp.remove_pipe("parser")

parser = nlp.create_pipe("parser")
nlp.add_pipe(parser, first=True)

for text, annotations in TRAIN_DATA:
    for dep in annotations.get("deps", []):
        parser.add_label(dep)

pipe_exceptions = ["parser", "trf_wordpiecer", "trf_tok2vec"]
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

# Load the model
model_name_DepHead = 'C:\Proyectos\AnalisiLogica\it_model_mons'

nlp = spacy.load(model_name_DepHead)

doc = nlp("Il cane di Lucia traffica nel giardino")

print([(t.text, t.dep_, t.head.text) for t in doc if t.dep_ != "-"])