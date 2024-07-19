import itertools
from basic_decor_library.Morph import Morph

class WordFormsGenerator:
    def __init__(self):
        self.morph = Morph()

    def generate_variations(self, phrase: str):
        words = phrase.split()
        all_forms = [self.morph.get_all_word_forms(word) for word in words]
        variations = list(itertools.product(*all_forms))
        
        return [" ".join(variation) for variation in variations]
