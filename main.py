from presentation.word import Word, FreeRelator
from presentation.poly import Poly
from presentation.tools import convert, combine, generate
from presentation.presentation import Presentation
from presentation.find import Search
import functools, itertools


from examples import exampleMannan


# y = Poly([(1,1)])
# one = Poly([(0,1)])
# some_polys = [functools.reduce(Poly.__add__, [(y**(n))*coeff[n] for n in range(0,4)]) for coeff in itertools.product(range(-1,2), repeat=4)]

if __name__=='__main__' and False:
    examples = []
    cases = []
    for p in some_polys:
        example = gen_path(p.poly)
        if not example in examples:
            examples.append(example)
            cases.append((example,p))
            print('\nExample: ', str(example), p, p.degree())

    cases.sort(key=lambda x: x[1].degree())
    print('Sorted')
    for exmp  in cases:
        print('\nExample: ',str(exmp[0]), exmp[1])
        find([exmp[0], Word('YxYxYXYYXY'[::-1])])

exampleMannan = list(map(Word.asFreeRelator, exampleMannan))
pres = Presentation(exampleMannan)
print(pres)

search = Search(pres)
# Search.sortFunction = lambda x: (len(x)+2*(x.height())**2, x.height())
Search.maxPoolSize = 20
search.findKleinRelator()
search.printPool()

print('[', ', '.join(map(str,search.pool)), ']')