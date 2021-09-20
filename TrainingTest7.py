import spacy
import random

model_name = 'C:\Proyectos\AnalisiLogica\it_model_mons'

nlp = spacy.load('it_core_news_sm')

TAG_MAP = {"N": {"pos": "NOUN"}, "V": {"pos": "VERB"}, "J": {"pos": "ADJ"}, "D": {"pos": "DET"}, "A": {"pos": "ADP"},
           "NUM": {"pos": "NUM"}}

TRAIN_DATA = [
    ("La fioritura delle rose dura per diversi mesi", {"words": ["D", "N", "D", "N", "V", "A", "D", "N"]}),
    ("Il film dura 6 ore", {"words": ["D", "N", "V", "NUM", "N"]}),
    ("Questa situazione dura da tempo", {"words": ["D", "N", "V", "A", "N"]}),

]



tagger = nlp.get_pipe("tagger")

#nlp.vocab.vectors.name = 'spacy_pretrained_vectors'

#for tag, values in TAG_MAP.items():
#    tagger.add_label(tag, values)

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'tagger']

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