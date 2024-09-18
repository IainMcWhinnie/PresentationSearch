from presentation.word import Word, Letter
from presentation.tools import convert
import functools

class Poly:
    def __init__(self, poly):
        self.poly = poly
    
    def __add__(self, other):
        return Poly(self.poly+other.poly)
    
    def __mul__(self, integer):
        return Poly([(term[0], integer*term[1]) for term in self.poly])

    def __pow__(self,integer):
        return Poly([(term[0]*integer, term[1]) for term in self.poly])

    def __neg__(self):
        return Poly([(term[0], term[1]*-1) for term in self.poly])
    
    def __str__(self):
        return ' + '.join([str(term[1])+'y^'+str(term[0]) for term in self.poly])
    
    def degree(self):
        lowest = 0
        highest = 0
        for term in self.poly:
            if term[0] > highest and term[1]!=0: highest = term[0]
            if term[0] < lowest and term[1]!=0: lowest = term[0]
        return highest-lowest


def gen_path(poly): #[(deg, coeff), ... ]
    paths = []
    for term in poly:
        conjugate = Word(Letter.multiple('y', term[0]))
        paths.append(Word.inverted(conjugate) + (convert('Xyxy')*term[1]) + conjugate)
    # paths = [combine(Word(''), convert('Xyxy'), 2, 0) for i in range(len(poly))]
    # print(list(map(str,paths)))
    # print(list(map(str,paths))  )
    return functools.reduce(Word.__add__,paths).reduce()