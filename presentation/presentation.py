from presentation.word import FreeRelator

class Presentation:
    def __init__(self, relators):
        for relator in relators:
            assert type(relator) == FreeRelator

        self.relators = relators
        self.isValidPresentation = False

    def __str__(self):
        return '< x,y | '+', '.join(map(str,self.relators))+' >'