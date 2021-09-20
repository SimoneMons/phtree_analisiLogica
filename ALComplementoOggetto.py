from ALTipoVerbo import tipo_frase

def find_complemento_oggetto(doc):

    phrase_type = tipo_frase(doc)

    articoli = ['il', 'lo', 'la', 'gli', 'le', 'i', 'un', 'uno', 'una', "un'"]

    pronomi_dimostrativi =['Questo', 'Questi', 'Questa', 'Queste', 'Quello', 'Quelli', 'Quella', 'Quelle',
                           'questo', 'questi', 'questa', 'queste', 'quello', 'quelli', 'quella', 'quelle']

    preposizioni_di_agente = ['da', 'dal', 'dallo', 'dalla', 'dai', 'dagli', 'dalle']

    for token in doc:

        if token.dep_ == 'obj' and doc[(token.i - 1)].text not in preposizioni_di_agente:
            if doc[(token.i - 1)].text in articoli or doc[(token.i - 1)].text in pronomi_dimostrativi:
                token._.complemento_oggetto = doc[(token.i - 1)].text + ' ' + token.text

            else:
                token._.complemento_oggetto = token.text

        else:
            token._.complemento_oggetto = ''

    return doc