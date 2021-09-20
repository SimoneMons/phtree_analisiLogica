

def find_predicato_nominale(doc):


    for token in doc:
        if token.pos_ == 'ADJ' and doc[(token.i-1)].lemma_ == 'essere':
            token._.predicato_nominale = doc[(token.i - 1)].text + ' ' + token.text
        else:
            token._.predicato_nominale = ''

    return doc