
class Letter:
    # must be between 26 and 97
    # 32 means inverses are capital letters
    inverse_ascii_difference = 32 # 32

    def parse(character):
        asciiCode = ord(character)
        if 97 <= asciiCode and asciiCode <= 122:
            return (character, False)
        else:
            return (chr(asciiCode + Letter.inverse_ascii_difference), True)
        
    def invert(character):
        character, inverse = Letter.parse(character)
        if inverse:
            return character
        else:
            return chr(ord(character) - Letter.inverse_ascii_difference)

    def multiple(character, pow):
        if pow >= 0:
            return character*pow
        else:
            return Letter.invert(character)*(-pow)

class Word:
    def __init__(self, word_str):
        self.word_str = word_str

    def reduce(self):
        self.word_str = Word.reduce_word(self.word_str)
        return self
    
    @classmethod
    def reduced(cls, word):
        return cls(Word.reduce_word(word.word_str))

    def reduce_word(word):
        prev_word = word
        word = Word.reduction_step(word)
        while word != prev_word:
            prev_word = word
            word = Word.reduction_step(word)
        return word

    def reduction_step(word):
        reduced_word = ''
        i = 0
        while i < len(word):
            if (i+1 < len(word)) and word[i] == Letter.invert(word[i+1]):
                i += 2
            else:
                reduced_word += word[i]
                i += 1
        return reduced_word

    def invert_word_string(word_string):
        return ''.join([Letter.invert(x) for x in word_string[::-1]])

    def invert(self):
        self.word_str = Word.invert_word_string(self.word_str)
        return self

    @classmethod
    def inverted(cls, word):
        return cls(Word.invert_word_string(word.word_str))

    def __str__(self):
        return self.word_str

    def __eq__(self, other):
        return self.word_str == other.word_str
    
    def __len__(self):
        return len(self.word_str)
            
    def __add__(self, other):
        return Word(self.word_str + other.word_str)
    
    def __mul__(self, integer):
        if integer >= 0:
            return Word(self.word_str*integer)
        else:
            return Word(Word.invert_word_string(self.word_str)*(-integer))
        
    def asFreeRelator(self):
        return FreeRelator(self.word_str)
    
    def height(self):
        cur_height = 0
        max_height = 0
        min_height = 0
        for char in self.word_str:
            if char == 'x': cur_height += 1
            elif char == 'X': cur_height -= 1
            
            if cur_height > max_height: max_height = cur_height
            if cur_height < min_height: min_height = cur_height
        return max_height-min_height
        

class FreeRelator(Word):
    def isCyclicRoation(word1, word2):
        assert len(word1) == len(word2)
        length = len(word1.word_str)

        for start_index in range(length):
            for offset in range(length):
                self_index = (start_index + offset)%length
                other_index = offset
                if word1.word_str[self_index] != word2.word_str[other_index]:
                    break
                elif offset == length-1:
                    return True
        return False
    
    def reduction_step(word):
        reduced_word = ''
        i = 0
        while i < len(word):
            if (i+1 < len(word)) and word[i] == Letter.invert(word[i+1]):
                i += 2
            else:
                reduced_word += word[i]
                i += 1
        if reduced_word != '' and reduced_word[0] == Letter.invert(reduced_word[-1]):
            reduced_word = reduced_word[1:-1]
        return reduced_word

    def __eq__(self, other):
        self.reduce()
        other.reduce()
        if len(self) != len(other.word_str): return False
        if len(self) == 0: return True

        return FreeRelator.isCyclicRoation(self,other) or FreeRelator.isCyclicRoation(self,Word.inverted(other))
    
    def __add__(self, other):
        return FreeRelator(self.word_str + other.word_str)
    
    def __mul__(self, integer):
        if integer >= 0:
            return FreeRelator(self.word_str*integer)
        else:
            return FreeRelator(Word.invert_word_string(self.word_str)*(-integer))
        