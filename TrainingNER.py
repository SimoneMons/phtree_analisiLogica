import spacy
import random
from spacy.util import minibatch, compounding

model_name = 'C:\Proyectos\AnalisiLogica\it_model_mons'

LABEL_TIME = "TIME"

LABEL_PLACE = "PLACE"


TRAIN_DATA = [
    ("Quest’anno la Pasqua cade in aprile", {"entities": [(29, 34, LABEL_TIME)]}),
    ("Filippo mi ha telefonato all’ora di pranzo", {"entities": [(29, 42, LABEL_TIME)]}),
    ("Atterreremo a Roma fra due ore", {"entities": [(19, 29, LABEL_TIME)]}),
    ("Vivono vicno alla stazione", {"entities": [(18, 25, LABEL_PLACE)]}),
    ("Sta mangiando a casa sua", {"entities": [(14, 23, LABEL_PLACE)]}),
    ("Facciamo un giro per la stazione", {"entities": [(24, 31, LABEL_PLACE)]}),
    ("Nell’acquario c’è un pesciolino rosso.", {"entities": [(0, 12, LABEL_PLACE)]}),
    ("Luca va all’università con i mezzi pubblici.", {"entities": [(8, 21, LABEL_PLACE)]}),
    ("Luca è tornato da Parigi.", {"entities": [(15, 23, LABEL_PLACE)]}),
    ("Entrai in garage e accesi il motore dell’auto.", {"entities": [(10, 15, LABEL_PLACE)]}),
    ("Laggiù è caduto un fulmine.", {"entities": [(0, 5, LABEL_PLACE)]}),
    ("Nella stazione c’è la mia postazione.", {"entities": [(6, 13, LABEL_PLACE)]}),
    ("Dentro c’è poca luce.", {"entities": [(0, 5, LABEL_PLACE)]}),
    ("Stazione", {"entities": [(0, 7, LABEL_PLACE)]}),
]

TRAIN_DATA = [
    (
        "Horses are too tall and they pretend to care about your feelings",
        {"entities": [(0, 6, LABEL)]},
    ),
    ("Do they bite?", {"entities": []}),
    (
        "horses are too tall and they pretend to care about your feelings",
        {"entities": [(0, 6, LABEL)]},
    ),
    ("horses pretend to care about your feelings", {"entities": [(0, 6, LABEL)]}),
    (
        "they pretend to care about your feelings, those horses",
        {"entities": [(48, 54, LABEL)]},
    ),
    ("horses?", {"entities": [(0, 6, LABEL)]}),
]


#nlp = spacy.blank('it')

#nlp = spacy.load('it_core_news_sm')

nlp = spacy.load(model_name)


if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
# otherwise, get it so we can add labels
else:
    ner = nlp.get_pipe("ner")


# add labels
ner.add_label(LABEL_PLACE)
ner.add_label(LABEL_TIME)

# Adding extraneous labels shouldn't mess anything up
ner.add_label("VEGETABLE")

#optimizer = nlp.resume_training()

optimizer = nlp.begin_training()

move_names = list(ner.move_names)
# get names of other pipes to disable them during training
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

n_iter = 6

disabled = nlp.disable_pipes('parser', 'tagger')
#with nlp.disable_pipes('parser', 'tagger'):  # only train NER
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
disabled.restore()
nlp.to_disk(model_name)

print(nlp.pipe_names)

nlp1 = spacy.load(model_name)

# test the trained model
#for text, _ in TRAIN_DATA:

doc = nlp1("Sono arrivato alla stazione con il taxi alle 8:35")
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
print("Tokens", [(token.text, token.i, token.lemma_, token.tag_, token.pos_, token.dep_, token.head.text,  token.head.pos_, token.ent_type_, token.ent_iob) for token in doc])



