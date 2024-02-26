class VocPreprocessor(object):
    def __init__(self, vocabulary, from_iterable=True, sep=' ',lowercase=True):
        self.vocabulary_=vocabulary
        self.from_iterable=from_iterable
        self.sep=sep
        self.lowercase=lowercase
    def preprocess(self, text):
        if not(self.from_iterable):
            text=text.split(self.sep)
        out=self.sep.join([self.vocabulary_[i] for i in text])
        if self.lowercase:
            return out.lower()
        else:
            return out
