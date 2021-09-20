

from ALTipoVerbo import tipo_frase

def find_soggetto(doc):

    phrase_type = tipo_frase(doc)

    soggetto = 0

    for token in doc:
        if token.dep_ == 'nsubj' or token.dep_ == 'nsubj:pass':
            soggetto = 1
            if doc[(token.i-1)].head.text == token.text:
                    token._.soggetto = doc[(token.i-1)].text + ' ' + token.text
            elif doc[(token.i+1)].dep_ == 'compound' and doc[(token.i+1)].head.text == token.text:
                    token._.soggetto = token.text + ' ' + doc[(token.i+1)].text
            else:
                    token._.soggetto = token.text


        # Soggetto sottinteso
        if soggetto == 0:
            if 'Person=2' in token.tag_:
                token._.soggetto = 'Tu, soggetto sottinteso'

            elif 'Person=1' in token.tag_ and 'Number=Sing' in token.tag_:
                token._.soggetto = 'Io, soggetto sottinteso'

            elif 'Person=1' in token.tag_ and 'Number=Plur' in token.tag_:
                token._.soggetto = 'Noi, soggetto sottinteso'

            elif 'Person=3' in token.tag_ and 'Number=Sing' in token.tag_:
                token._.soggetto = 'Lui - Lei, soggetto sottinteso'

            elif 'Person=3' in token.tag_ and 'Number=Plur' in token.tag_:
                token._.soggetto = 'Loro, soggetto sottinteso'

    return doc