import nltk
from nltk.corpus import wordnet


class Word:

    def __init__(self, word_text):
        self.text = word_text
        self.synonyms = []
        self.antonyms = []
        self.wnset = ""
        self.pos = ""
<<<<<<< HEAD
=======
        self.lemma = ""
>>>>>>> bed7897f7a5953cda7c4c444f5631eee570f17f1
        self.definitionDict = {}
        self.get_pos(self)
        self.get_syn_ant_def(self)
        self.lemmatize(self)

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
                word.definitionDict[syns] = syns.definition()
                if synonym.antonyms():
                    word.antonyms.append(synonym.antonyms()[0].name())
<<<<<<< HEAD
=======

    @staticmethod
    def lemmatize(word):
        lemmatizer = WordNetLemmatizer()
        if word.pos != '':
            word.lemma = lemmatizer.lemmatize(word.text, word.pos)
        else:
            word.lemma = lemmatizer.lemmatize(word.text)

    # this method returns the output of the famous soundEx algorithm (Odell and Russell, 1922; Knuth 1973) for the given text
    def soundex(self):
        # Drop letters
        drop_letters = ["a", "e", "h", "i", "o", "u", "w", "y"]
        # Number-character map
        number_character_map = [['b', 'f', 'p', 'v'], ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z'],
                                ['d', 't'], ['l'], ['m', 'n'], ['r']]
        final_word = self.text[0]
        not_dropped = [letter for letter in self.text[1:] if letter not in drop_letters]
        for letter in not_dropped:
            for index in range(len(number_character_map)):
                if letter in number_character_map[index]:
                    final_word += str(index+1)
        if len(final_word) > 4:
            return final_word[0:4]
        else:
            return final_word + ("0" * (4-len(final_word)))
>>>>>>> bed7897f7a5953cda7c4c444f5631eee570f17f1
