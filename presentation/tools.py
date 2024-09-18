from presentation.word import Word, Letter, FreeRelator

def convert(genString):
    word = ''
    i = 0
    while i < len(genString):
        letter = genString[i]
        if i+1 < len(genString) and genString[i+1] == '*':
            letter = Letter.invert(letter)
            i += 1
        word += letter
        i += 1
    return Word(word)

def combine(path1, path2, offx, offy):
    ## Conjugate path2 to put it where offset specifies
    conjugate = Word(Letter.multiple('x', offy) + Letter.multiple('y', offx))
    return FreeRelator.reduced(conjugate + Word.inverted(path2) + Word.inverted(conjugate) + path1)

def generate(path1, path2):
    newPaths = []
    max_conjugation_size = 4
    for i in range(-max_conjugation_size,max_conjugation_size+1):
        for j in range(-max_conjugation_size,max_conjugation_size+1):
            if path1 != path2 or (i,j) != (0,0):
                newPath = combine(path1, path2, i ,j)
                newPaths.append(newPath)

                newPath = combine(path1, Word.inverted(path2), i, j)
                newPaths.append(newPath)
    return newPaths