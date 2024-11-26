from Sentence import Sentence

class Parser:
    def __init__(self):
        self.articles = ["the ", "a ", "an "]
        self.prepositions = ["with","in","on","under","over"]
        self.debug = True

    def parse(self,sentence):
        v = None
        do = None
        io = None
        for article in self.articles:
            sentence = sentence.replace(article, "")
        for preposition in self.prepositions:
            if preposition in sentence:
                if not io:
                    parts = sentence.split(preposition)
                    io = parts[1]
                    io = io.lstrip()
                    sentence = parts[0]
                else:
                    raise ValueError("too many indirect objects")
        parts = sentence.split()
        v = parts[0]
        if len(parts)>1:
            do = " ".join(parts[1:])
        if self.debug:
            print("parsed sentence: verb =",v,"do =",do, "io =",io)
        return Sentence(v,do,io)