
from ReadFile import read_verbi_intransitivi

def tipo_frase(doc):

    verbi_intransitivi = read_verbi_intransitivi()

    subjpass = 0

    for tok in doc:
        if tok.pos_ == 'VERB':
            if tok.lemma_ in verbi_intransitivi:
                #Frase attiva
                subjpass = 0

            elif 'VerbForm=Fin' in tok.tag_:
                subjpass = 0

            elif doc[(tok.i - 1)].dep_ == 'aux:pass' and 'VerbForm=Part' in tok.tag_:
                #Frase passiva
                subjpass = 1

    return subjpass