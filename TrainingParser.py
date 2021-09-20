import spacy
import random

model_name = 'C:\Proyectos\AnalisiLogica\it_model_mons'

#nlp = spacy.load('it_core_news_sm')

nlp = spacy.load(model_name)


# training data
TRAIN_DATA = [
    (
        "La fioritura delle rose dura per diversi mesi",
        {
            "heads": [1, 1, 3, 1, 1, 4, 4, 4],
            "deps": ["det", "nsubj", "det", "obj", "ROOT", "case", "det", "obj"],
        },
    ),
]


parser = nlp.get_pipe("parser")


other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'parser']

n_iter = 10

with nlp.disable_pipes(*other_pipes):
    nlp.vocab.vectors.name = 'spacy_pretrained_vectors'
    optimizer = nlp.begin_training()
    for i in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            nlp.update([text], [annotations], sgd=optimizer, losses=losses)
        print(losses)


#Save the model
nlp.to_disk(model_name)

nlp = spacy.load(model_name)

doc = nlp("La fioritura delle rose dura per diversi mesi")

for token in doc:
    print(token.text, token.i, token.lemma_, token.tag_, token.pos_, token.dep_, token.head.text,  token.head.pos_)