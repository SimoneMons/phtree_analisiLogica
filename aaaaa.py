import spacy
import random
from spacy.util import minibatch, compounding

model_name = 'C:\Proyectos\AnalisiLogica\it_model_mons'



LABEL_PLACE = "PLACE"
LABEL_TIME = "TIME"


TRAIN_DATA = [
    ("Vivono vicno alla stazione", {"entities": [(18, 25, LABEL_PLACE)]}),
    ("Facciamo un giro per la stazione", {"entities": [(24, 31, LABEL_PLACE)]}),
    ("Nella stazione c’è la mia postazione.", {"entities": [(6, 13, LABEL_PLACE)]}),
    ("Stazione", {"entities": [(0, 7, LABEL_PLACE)]}),
]

#nlp = spacy.blank('it')

#nlp = spacy.load('en_core_web_sm')
#nlp = spacy.load(model_name)

nlp = spacy.load('it_core_news_sm')

if "ner" not in nlp.pipe_names:
    ner = nlp.create_pipe("ner")
    nlp.add_pipe(ner)
# otherwise, get it, so we can add labels to it
else:
    ner = nlp.get_pipe("ner")

n_iter = 10

ner.add_label(LABEL_TIME)  # add new entity label to entity recognizer
ner.add_label(LABEL_PLACE)  # add new entity label to entity recognizer

# Adding extraneous labels shouldn't mess anything up
ner.add_label("VEGETABLE")

optimizer = nlp.begin_training()
#optimizer = nlp.resume_training()

move_names = list(ner.move_names)
# get names of other pipes to disable them during training
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
with nlp.disable_pipes(*other_pipes):  # only train NER
        sizes = compounding(1.0, 4.0, 1.001)
        # batch up the examples using spaCy's minibatch
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            batches = minibatch(TRAIN_DATA, size=sizes)
            losses = {}
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
            print("Losses", losses)


#Save the model
#disabled.restore()
nlp.to_disk(model_name)

print(nlp.pipe_names)

nlp1 = spacy.load(model_name)

# test the trained model
for text, _ in TRAIN_DATA:
    doc = nlp1(text)
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    print("Tokens", [(token.text, token.i, token.lemma_, token.tag_, token.pos_, token.dep_, token.head.text,  token.head.pos_, token.ent_type_, token.ent_iob) for token in doc])



