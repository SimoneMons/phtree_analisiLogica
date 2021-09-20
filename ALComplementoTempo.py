def find_complemento_tempo(doc):

    tempo_determinato = ['a', 'da', 'in', 'su', 'sui', 'per', 'presso', 'sotto', 'sopra', 'su', 'sul', 'sulla', "sull'"]

    tempo_continuato = ['a', 'da', 'in', 'su', 'sui', 'per', 'presso', 'sotto', 'sopra', 'su', 'sul', 'sulla', "sull'"]

    for tokl in doc:
        if (doc[(tokl.i - 1)].text in tempo_continuato or doc[(tokl.i - 2)].text in tempo_determinato)\
                and tokl.dep_ == 'TIME'\
                and tokl.pos_ not in ('VERB'):
            tokl._.complemento_tempo = doc[(tokl.i - 1)].text + ' ' + tokl.text
            print(tokl._.complemento_tempo)
        else:
            tokl._.complemento_tempo = ''

    return doc