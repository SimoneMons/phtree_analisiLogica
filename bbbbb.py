
import textacy
about_talk_text = ('The talk will introduce reader about Use'
                    ' cases of Natural Language Processing in'
                    ' Fintech')
pattern = r'(<VERB>?<ADV>*<VERB>+)'
about_talk_doc = textacy.make_spacy_doc(about_talk_text, lang='en_core_web_sm')
verb_phrases = textacy.extract.pos_regex_matches(about_talk_doc, pattern)
# Print all Verb Phrase
for chunk in verb_phrases:
    print(chunk.text)