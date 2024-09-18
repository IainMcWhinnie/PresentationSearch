from presentation.word import Word, convert, Letter
import itertools

def generate(path1, path2):
    newPaths = []
    max_conjugation_size = 4
    for i in range(-max_conjugation_size,max_conjugation_size+1):
        for j in range(-max_conjugation_size,max_conjugation_size+1):
            for k in range(-max_conjugation_size, max_conjugation_size):

                if path1 != path2 or (i,j,k) != (0,0,0):
                    conjugate = Word(Letter.multiple('x', j) + Letter.multiple('y', i) + Letter.multiple('z', k))

                    newPaths.append(Word.reduced(conjugate + Word.inverted(path2) + Word.inverted(conjugate) + path1))

                    newPaths.append(Word.reduced(conjugate + path2 + Word.inverted(conjugate) + path1))

    return list(map(commReduceWord, newPaths))


def find(pool, target):
    pool = list(map(commReduceWord, pool))
    original_pool = pool[:]
    maxPoolSize = 50
    noAddedEachRound = maxPoolSize
    sort_function = len

    pool.sort(key=sort_function)

    worst_in_pool = sort_function(pool[-1])
    best_newcomer = ()

    for stageNo in range(100):
        print('\nStage:',stageNo)
        print('\tCurrently', len(pool), 'paths in the pool')
        print('\tThe scores are ',[sort_function(x) for x in pool])
        worst_in_pool = sort_function(pool[-1])
        for oldy in original_pool:
            if not oldy in pool:
                pool.append(oldy)

        try:
            potential = []
            for i in range(len(pool)):
                for j in range(i,len(pool)):
                    potential += generate(pool[i], pool[j])
        except KeyboardInterrupt:
            print('\tInterrupted by the keyboard.')
            break


        potential.sort(key=sort_function)
        print('\tThere are', len(potential), 'potential new relations.')
        print('\tThe best', str(potential[0]), 'has a score of ', sort_function(potential[0]), 'and the worst had a score of ', sort_function(potential[-1]))


        print('\tAdding relations with scores: ',end='')
        i = 0
        for new_relation in potential:
            if not (new_relation in pool or Word.inverted(new_relation) in pool) :
                if i == 0:
                    best_newcomer = sort_function(new_relation)               
                pool.append(new_relation)
                print(sort_function(new_relation),' ',end='')
                i += 1
            if i == noAddedEachRound:
                break
        del potential
        print('')

        if sorted([best_newcomer, worst_in_pool])[0] == worst_in_pool and stageNo != 0:
            print('\tThe program has reached its limits. Further iteration will provide the same results. Exiting.')
            break

        pool.sort(key=sort_function)
        # if len(pool[0])==4:
        #     print('\n\n','#'*50,'\n\t\tHOLY MACARONI YOU FOUND IT!!!!!!')
        #     print('original pool was', [str(x) for x in original_pool],'\n\n', '#'*50)
        #     with open('test.txt','a') as f:
        #         f.write(str([str(x) for x in original_pool])+'\n')
        #     break

        print([target_rel in pool or Word.inverted(target_rel) in pool for target_rel in target])
        if all([target_rel in pool or Word.inverted(target_rel) in pool for target_rel in target]):
            print('Found')
            print('\n\n','#'*50,'\n\t\tHOLY MACARONI YOU FOUND IT!!!!!!')
            print('\t\toriginal pool was', [str(x) for x in original_pool],'\n\n', '#'*50)
            with open('test1.txt','a') as f:
                f.write(str([str(x) for x in original_pool])+'\n')
            break

        if len(pool) > maxPoolSize:
            print('\tCulling worst scoring relations until the pool size is', maxPoolSize)
            pool = pool[:maxPoolSize]


    pool.sort(key=len)
    print('\nThe final scores are ',[sort_function(x) for x in pool])
    print([str(x) for x in pool])

class Poly2:
    def __init__(self, poly): # Poly = [(deg_y, deg_z, coeff), ...]
        self.poly = poly
    
    def __add__(self, other):
        return Poly2(self.poly+other.poly)
    
    def __mul__(self, other):
        if type(other) == int:
            return Poly2([(term[0], term[1], other*term[2]) for term in self.poly])
        else:
            return Poly2([(self_term[0]+other_term[0], self_term[1]+other_term[1], self_term[2]*other_term[2]) for self_term, other_term in itertools.product(self.poly, other.poly)])

    def __pow__(self,integer):
        return Poly2([(term[0]*integer, term[1]*integer, term[2]) for term in self.poly])

    def __neg__(self):
        return Poly2([(term[0], term[1], term[2]*-1) for term in self.poly])
    
    def __str__(self):
        return ' + '.join([str(term[2])+'y^'+str(term[0])+'z^'+str(term[1]) for term in self.poly])
    
    def degree(self):
        lowest = 0
        highest = 0
        for term in self.poly:
            if term[0]+term[1] > highest and term[2]!=0: highest = term[0]+term[1]
            if term[0]+term[1] < lowest and term[2]!=0: lowest = term[0]+term[1]
        return highest-lowest

y = Poly2([(1,0,1)])
z = Poly2([(0,1,1)])

some_polys = [ y**y_deg*z**z_deg*coeff
              for y_deg, z_deg, coeff in itertools.product(range(0,4), range(0,4), range(-1,2))]

def commReduce(relation):
    absoluteSplit = list(map(lambda x: x.split('X'), relation.split('x')))
    newSplitinx = []
    for splitinx in absoluteSplit:
        newSplitinX = []
        for splitinX in splitinx:
            ys = splitinX.count('y')-splitinX.count('Y')
            zs = splitinX.count('z')-splitinX.count('Z')
            newSplitinX.append(Letter.multiple('z',zs)+Letter.multiple('y',ys))
        newSplitinx.append('X'.join(newSplitinX))
    return 'x'.join(newSplitinx)

def commReduceWord(word):
    return Word(commReduce(word.word_str))

# print(list(map(str,some_polys)))
# print(commReduce('zYZxZYzX'))
# convert('z*y*zy'), 
find([convert('zy*z*xz*y*zx*')], [convert('x*yxy'), convert('x*zxz')])