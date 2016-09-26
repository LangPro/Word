import nltk
from nltk.corpus import wordnet


class Word:

    def __init__(self, word_text):
        self.text = word_text
        self.synonyms = []
        self.antonyms = []
        self.wnset = ""
        self.pos = ""
        self.definitionList = {}
        self.get_pos(self)
        self.get_syn_ant_def(self)

    # gets the nltk POS and then uses the mapper function to map to wordnet POS
    @staticmethod
    def get_pos(word):
        tag = nltk.pos_tag(word.text.split(" "))[0][1]
        word.pos = word.wn_pos_mapper(tag)

    # maps nltk POS tags to wordnet POS tags
    @staticmethod
    def wn_pos_mapper(tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('V'):
            return wordnet.VERB
        elif tag.startswith('N'):
            return wordnet.NOUN
        elif tag.startswith('R'):
            return wordnet.ADV
        elif tag.startswith('S'):
            return wordnet.ADJ_SAT
        else:
            return ''

    # this method will use nltk wordnet to find synonyms, antonyms, and definition for stored word
    @staticmethod
    def get_syn_ant_def(word):
        # get synsets for word
        ssets = wordnet.synsets(word.text)
        for syns in ssets:
            for synonym in syns.lemmas():
                word.synonyms.append(synonym.name())
                word.definitionList[syns] = syns.definition()
                if synonym.antonyms():
                    word.antonyms.append(synonym.antonyms()[0].name())
                    