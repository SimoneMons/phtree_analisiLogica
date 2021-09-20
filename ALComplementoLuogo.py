def find_complemento_luogo(doc):

    preposizioni_luogo = ['a', 'da', 'in', 'su', 'sui', 'per', 'presso', 'sotto', 'sopra', 'su', 'sul', 'sulla', "sull'", 'di', 'da']

    for tokl in doc:
        if (doc[(tokl.i - 1)].text in preposizioni_luogo or doc[(tokl.i - 2)].text in preposizioni_luogo)\
                and tokl.dep_ == 'PLACE'\
                and tokl.pos_ not in ('VERB'):
            tokl._.complemento_luogo = doc[(tokl.i - 1)].text + ' ' + tokl.text
            print(tokl._.complemento_luogo)
        else:
            tokl._.complemento_luogo = ''

    return doc