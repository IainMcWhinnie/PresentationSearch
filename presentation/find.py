from presentation.tools import generate
from presentation.word import Word, FreeRelator
from presentation.tools import convert

class Search:
    maxPoolSize = 20
    noAddedEachRound = maxPoolSize
    sortFunction = len
    DEBUG = True

    def __init__(self, presentation):
        self.presentation = presentation
        self.pool = presentation.relators

    def getPotentialRels(pool):
        potential = []
        for i in range(len(pool)):
            for j in range(i,len(pool)):
                for newRel in generate(pool[i], pool[j]):
                    if newRel != FreeRelator(''):
                        potential.append(newRel)
        potential.sort(key=Search.sortFunction)
        return potential
    
    def getUniqueRels(self, potential, n):
        uniqueRels = []
        i = 0
        for rel in potential:
            if not rel in self.pool and not rel in uniqueRels:
                uniqueRels.append(rel)
                i += 1
            if i == n:
                break
        uniqueRels.sort(key=Search.sortFunction)
        return uniqueRels

    def performSearchRound(self):
        self.log('Performing search round...')
        worstScore = max(map(Search.sortFunction, self.pool))

        potential = Search.getPotentialRels(self.pool)
        self.log('\tFound', len(potential), 'possible relators')

        relsToAdd = self.getUniqueRels(potential, Search.noAddedEachRound)
        if len(relsToAdd) != 0 and Search.sortFunction(relsToAdd[1]) < worstScore or len(self.pool) != Search.maxPoolSize:
            self.pool += relsToAdd
            self.log('\tAdded', len(relsToAdd), 'new relations to the pool')
        else:
            self.log('\tThe program has reached its limits. Further iteration will provide the same results. Exiting.')
            return False

        self.pool.sort(key=Search.sortFunction)

        if len(self.pool) > Search.maxPoolSize:
            self.pool = self.pool[:Search.maxPoolSize]
        return True

    def findKleinRelator(self):
        kleinRelator = convert('Xyxy').asFreeRelator()
        self.pool.sort(key=Search.sortFunction)

        # worstInPool = self.pool[-1]
        for i in range(20):
            if not self.performSearchRound():
                break
            if kleinRelator in self.pool:
                print('FOUND KLEIN RELATOR')
                return True
            self.printPool()

        return False

    def findRelator(self, relator):
        self.pool.sort(key=Search.sortFunction)
        for i in range(20):
            if not self.performSearchRound():
                break
            if relator in self.pool:
                print('Found relator')
                break
            self.printPool()
        

    def printPool(self):
        print('[', ', '.join(map(lambda x: str(Search.sortFunction(x)),self.pool)), ']')
    
    def log(self, *args, **kwargs):
        if Search.DEBUG:
            print(*args, **kwargs)

# def find(pool):
#     original_pool = pool[:]
#     maxPoolSize = 50
#     noAddedEachRound = maxPoolSize
#     sort_function = lambda x: (len(x)+2*(x.height())**2, x.height())

#     pool.sort(key=sort_function)

#     worst_in_pool = sort_function(pool[-1])
#     best_newcomer = ()

#     for stageNo in range(100):
#         print('\nStage:',stageNo)
#         print('\tCurrently', len(pool), 'paths in the pool')
#         print('\tThe scores are ',[sort_function(x) for x in pool])
#         worst_in_pool = sort_function(pool[-1])
#         for oldy in original_pool:
#             if not oldy in pool:
#                 pool.append(oldy)

#         try:
#             potential = []
#             for i in range(len(pool)):
#                 for j in range(i,len(pool)):
#                     potential += generate(pool[i], pool[j])
#         except KeyboardInterrupt:
#             print('\tInterrupted by the keyboard.')
#             break


#         potential.sort(key=sort_function)
#         print('\tThere are', len(potential), 'potential new relations.')
#         print('\tThe best', str(potential[0]), 'has a score of ', sort_function(potential[0]), 'and the worst had a score of ', sort_function(potential[-1]))


#         print('\tAdding relations with scores: ',end='')
#         i = 0
#         for new_relation in potential:
#             if not (new_relation in pool or Word.inverted(new_relation) in pool) :
#                 if i == 0:
#                     best_newcomer = sort_function(new_relation)               
#                 pool.append(new_relation)
#                 print(sort_function(new_relation),' ',end='')
#                 i += 1
#             if i == noAddedEachRound:
#                 break
#         del potential
#         print('')

#         if sorted([best_newcomer, worst_in_pool])[0] == worst_in_pool and stageNo != 0:
#             print('\tThe program has reached its limits. Further iteration will provide the same results. Exiting.')
#             break

#         pool.sort(key=sort_function)
#         if len(pool[0])==4:
#             print('\n\n','#'*50,'\n\t\tHOLY MACARONI YOU FOUND IT!!!!!!')
#             print('original pool was', [str(x) for x in original_pool],'\n\n', '#'*50)
#             with open('test.txt','a') as f:
#                 f.write(str([str(x) for x in original_pool])+'\n')
#             break

#         if len(pool) > maxPoolSize:
#             print('\tCulling worst scoring relations until the pool size is', maxPoolSize)
#             pool = pool[:maxPoolSize]


#     pool.sort(key=len)
#     print('\nThe final scores are ',[sort_function(x) for x in pool])
#     print([str(x) for x in pool])

