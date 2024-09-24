import unittest

from presentation.word import Letter, Word, FreeRelator

class TestLetter(unittest.TestCase):

    def test_parse(self):
        assert Letter.parse('x') == ('x', False)
        assert Letter.parse('X') == ('x', True)

    def test_invert(self):
        assert Letter.invert('x') == 'X'
        assert Letter.invert('X') == 'x'

    def test_multiple(self):
        assert Letter.multiple('x', 3) == 'xxx'
        assert Letter.multiple('x', -4) == 'XXXX'

class TestWord(unittest.TestCase):

    def test_reduce_1(self):
        word1 = Word('xxyYXyYyYXx')
        word1.reduce()
        assert word1 == Word('x')

    def test_reduce_2(self):
        word2 = Word('xyXyYX')
        assert Word.reduced(word2) == Word('xyXX')

    def test_invert_1(self):
        word = Word('xyyYXyxyxyYX')
        word.invert()
        assert word == Word('xyYXYXYxyYYX')

    def test_invert_2(self):
        word = Word('yXyYxXyYxY')
        assert Word.inverted(word) == Word('yXyYxXyYxY')

    def test_len(self):
        assert len(Word('xxxxx')) == 5

    def test_add(self):
        assert Word('xyx')+Word('YXY') == Word('xyxYXY')

    def test_mul_1(self):
        assert Word('xYX')*4 == Word('xYXxYXxYXxYX')
    
    def test_mul_2(self):
        assert Word('Yx')*(-2) == Word('XyXy')

    def test_asFreeRelator(self):
        rel = Word('xYxxyxyYXyx').asFreeRelator()
        assert type(rel) == FreeRelator
        assert rel == FreeRelator('xYxxyxyYXyx')


class TestFreeRelator(unittest.TestCase):
    
    def test_reduce_1(self):
        word2 = FreeRelator('xXyYX')
        assert Word.reduced(word2) == Word('X')

    def test_reduce_2(self):
        word = FreeRelator('xXyYX')
        word.reduce()
        assert word == Word('X')

    def test_reduce_3(self):
        word = FreeRelator('xXyYX')
        assert Word.reduced(word) == Word('X')

    def test_reduce_4(self):
        word = FreeRelator('xYX')
        word.reduce()
        assert word == FreeRelator('Y')

    def test_reduced(self):
        word = FreeRelator('xyxxxYXxxYXYX')
        assert type(FreeRelator.reduced(word)) == FreeRelator

    def test_inverted(self):
        word = FreeRelator('xYXxyxyXYYXYXYyxy')
        assert type(FreeRelator.inverted(word)) == FreeRelator

    def test_add(self):
        assert type(FreeRelator('xyxyYYX')+FreeRelator('XyXYyXy')) == FreeRelator

    def test_eq_1(self):
        assert FreeRelator('xYYx') == FreeRelator('YYxx')

    def test_eq_2(self):
        assert FreeRelator('xyxxyxyyyxyYX') == FreeRelator('xxyxyyyxy')

    def test_eq_3(self):
        assert FreeRelator('xX') == FreeRelator('')

    def test_eq_4(self):
        assert FreeRelator('yyxYYXYXyyyx') == FreeRelator.reduced(FreeRelator('XXYYYxyxyyXYYx'))

    def test_eq_5(self):
        assert FreeRelator('XXYYYxyxyyXYYx') == FreeRelator('yyxYYXYXyyyx')
