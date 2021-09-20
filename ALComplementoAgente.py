from ALTipoVerbo import tipo_frase

def find_complemento_agente(doc):

    phrase_type = tipo_frase(doc)

    preposizioni_di_agente = ['da', 'dal', 'dallo', 'dalla', 'dai', 'dagli', 'dalle']


    for token in doc:
        if (token.dep_ == 'obl:agent' or token.dep_ == 'obj') and doc[(token.i - 1)].text in preposizioni_di_agente:
                token._.complemento_agente = doc[(token.i - 1)].text + ' ' +token.text

    return doc


