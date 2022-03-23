import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """Instantiates wordfinder and creates wordlist from file"""
        self.filepath = filepath
        self.wordlist = self.get_wordlist()


    def __repr__(self):
        return f"<WordFinder wordlist={self.wordlist} filepath={self.filepath}>"
    
    def get_wordlist(self):
        """Takes file of words and returns words in a list"""
        wordfile = open(self.filepath)
        wordlist = [line.replace('\n', '') for line in wordfile]
        return wordlist
    
    def random(self):
        """Returns a random word from a list of words"""
        return random.choice(self.wordlist)
       
wf = WordFinder('words.txt')



class SpecialWordFinder(WordFinder):
    """DOCSTRING"""

    def __init__(self, filepath):
        """Instantiates a special word finder that cleans up list of words"""
        super().__init__(filepath)
        self.wordlist = self.refine_list()

    def refine_list(self):
        """Takes wordlist and strips empty lines and comments"""
        # ['# Veggies', '', 'kale', 'parsnips', '', '# Fruits', etc]
        new_word_list = [word for word in self.wordlist if word]
        new_word_list = [word for word in new_word_list if not word.startswith('#')]
        return new_word_list


swf = SpecialWordFinder('fancywords.txt')
