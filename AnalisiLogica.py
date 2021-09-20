import spacy

from spacy.tokens import Doc, Token, Span
from ALSoggetto import find_soggetto
from ALPredicatoVerbale import find_predicato_verbale
from ALPredicatoNominale import find_predicato_nominale
from ALComplementoOggetto import find_complemento_oggetto
from ALComplementoLuogo import find_complemento_luogo
from ALComplementoSpecificazioneCausa import find_complemento_specificazione_causa
from ALComplementoTempo import find_complemento_tempo
from ALComplementoAgente import find_complemento_agente

def main ():

    # Load the model
    model_name = 'C:\Proyectos\AnalisiLogica\it_model_mons'

    model_name_place = 'C:\Proyectos\AnalisiLogica\it_model_mons_place'

    model_name_time = 'C:\Proyectos\AnalisiLogica\it_model_mons_time'

    #nlp = spacy.load('it_core_news_sm')
    nlp = spacy.load(model_name)

    #print(nlp.pipeline)

    # Soggetto
    nlp.add_pipe(find_soggetto, name="Soggetto", last=True)
    Token.set_extension('soggetto', default=False)


    # Predicato Verbale
    nlp.add_pipe(find_predicato_verbale, name="Predicato verbale", last=True)
    Token.set_extension('predicato_verbale', default=False)

    # Predicato Nominale
    nlp.add_pipe(find_predicato_nominale, name="Predicato nominale", last=True)
    Token.set_extension('predicato_nominale', default=False)

    #Complementi
    nlp.add_pipe(find_complemento_specificazione_causa, name="Complemento di specificazione", last=True)
    Token.set_extension('complemento_specificazione', default=False)

    nlp.add_pipe(find_complemento_specificazione_causa, name="Complemento di causa", last=True)
    Token.set_extension('complemento_causa', default=False)

    nlp.add_pipe(find_complemento_agente, name="Complemento d'agente", last=True)
    Token.set_extension('complemento_agente', default=False)

    nlp.add_pipe(find_complemento_oggetto, name="Complemento oggetto", last=True)
    Token.set_extension('complemento_oggetto', default=False)



    # Frase da analizzare
    text = "La fioritura delle rose dura per diversi mesi"


    doc = nlp(text)

    for token in doc:
        print(token.text, token.i, token.lemma_, token.tag_, token.pos_, token.dep_, token.head.text,  token.head.pos_)

    print(spacy.explain('obl'))

    #Print analisys logica
    for token in doc:
        if token._.soggetto:
            print(token._.soggetto, '-->', ' Soggetto')

        if token._.predicato_verbale:
            print(token._.predicato_verbale, '-->', ' Predicato verbale')

        if token._.predicato_nominale:
            print(token._.predicato_nominale, '-->', ' Predicato nominale')

        if token._.complemento_oggetto:
            print(token._.complemento_oggetto, '-->', ' Complemento oggetto')

        if token._.complemento_specificazione:
            print(token._.complemento_specificazione, '-->', ' Complemento di specificazione')

        if token._.complemento_causa:
            print(token._.complemento_causa, '-->', ' Complemento di causa')

        if token._.complemento_agente:
            print(token._.complemento_agente, '-->', " Complemento d'agente")



    #load models
    nlp_mons_model_place = spacy.load(model_name_place)
    nlp_mons_model_time = spacy.load(model_name_time)


    #Complemento di luogo
    nlp_mons_model_place.add_pipe(find_complemento_luogo, name="Complemento di luogo", last=True)
    Token.set_extension('complemento_luogo', default=False)

    doc_mons_model_place = nlp_mons_model_place(text)

    for tokl in doc_mons_model_place:
        #print(tokl.text, tokl.i, tokl.lemma_, tokl.tag_, tokl.pos_, tokl.dep_, tokl.head.text,  tokl.head.pos_)
        if tokl._.complemento_luogo:
            print(tokl._.complemento_luogo, '-->', ' Complemento di luogo')


    #Complemento di tempo
    nlp_mons_model_time.add_pipe(find_complemento_tempo, name="Complemento di tempo", last=True)
    Token.set_extension('complemento_tempo', default=False)

    doc_mons_model_time = nlp_mons_model_time(text)

    for tokt in doc_mons_model_time:
        #print(tokt.text, tokt.i, tokt.lemma_, tokt.tag_, tokt.pos_, tokt.dep_, tokt.head.text,  tokt.head.pos_)
        if tokt._.complemento_tempo:
            print(tokt._.complemento_tempo, '-->', ' Complemento di tempo')


main()
