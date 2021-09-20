
from ReadFile import read_verbi_riflessivi

def find_predicato_verbale(doc):

    verbi_riflessivi = []

    verbi_riflessivi = read_verbi_riflessivi()

    for token in doc:
        if token.pos_ == 'VERB' and ('VerbForm=Part' in token.tag_ or 'VerbForm=Inf' in token.tag_):
            if doc[(token.i-1)].dep_ in ('aux:pass', 'aux') and doc[(token.i-1)].pos_ == 'AUX':
                if doc[(token.i-2)].dep_ == 'aux' and doc[(token.i-2)].pos_ == 'AUX':
                    token._.predicato_verbale = doc[(token.i-2)].text + ' ' + doc[(token.i-1)].text + ' ' + \
                                                    token.text
                elif doc[(token.i-1)].dep_ in ('aux:pass', 'aux') and doc[(token.i-1)].head.text == token.text:
                        token._.predicato_verbale = doc[(token.i - 1)].text + ' ' + token.text

        elif token.pos_ == 'VERB' and doc[(token.i-1)].text in ("c'", "c’"):
            token._.predicato_verbale = doc[(token.i - 1)].text + token.text

        elif token.pos_ == 'VERB':
            token._.predicato_verbale = token.text


        elif token.text in verbi_riflessivi:
            token._.predicato_verbale = token.text

    return doc