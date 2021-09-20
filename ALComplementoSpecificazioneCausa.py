

def find_complemento_specificazione_causa(doc):

    preposizioni_di_specificazione = ['di', 'del', 'della', 'dei', 'degli', 'delle']

    preposizioni_di_causa =['da', 'dal', 'dallo', 'dalla', 'dai', 'dagli', 'dalle']

    for token in doc:
        if token.dep_ in ('obj', 'obl', 'nmod', 'nsubj:pass', 'amod') and token.pos_ in ('NOUN', 'PROPN'):
            if doc[(token.i - 1)].text in preposizioni_di_specificazione:
                token._.complemento_specificazione = doc[(token.i - 1)].text + ' ' +token.text
            elif doc[(token.i - 1)].text in preposizioni_di_causa:
                token._.complemento_causa = doc[(token.i - 1)].text + ' ' +token.text
        else:
            token._.complemento_specificazione = ''
            token._.complemento_causa = ''


    return doc

