from presentation.tools import convert
from presentation.word import Word

example1 = [convert('x*yyxy*x*yxyyyy'), convert('yyyx*yxy*x*x*y*xyxy')]
example2 = [convert('yyxyyx*'),convert('xxy*x*x*y')]
example3 = [convert('x*x*yxxy*'), convert('yyyyxyx*y*xyyx*')]
example4 = [convert('x*x*yxxy*'), convert('yyxy*y*x*y*y*y*xyx*')] # works
example5 = [convert('x*x*yxxy*'), convert('yyyyxyx*y*y*xyx*')]
example6 = [convert('x*x*yxxy*'), Word.inverted(convert('yyyxy*x*y*y*y*xyx*'))]
example7 = [convert('x*x*yxxy*'), convert('yxy*xy*x*yx*')]
example8 = [convert('x*x*x*yxxxy*'), convert('y*y*y*x*yxyyx*y*y*x')]
example9 = [convert('y*x*y*x*yxxy*'), convert('y*y*y*x*yxyyx*y*y*x')] # works, yay
example10 = [convert('y*x*y*x*yxxy*'), convert('yyxy*y*x*y*y*y*xyx*')] #works
example11 = [convert('y*x*y*x*yxxy*'), convert('yyyyxyx*y*xyyx*')]
example12 = [convert('yxyxy*x*yx*yy'), convert('y*y*y*x*yxyyx*y*y*x')]
example13 = [convert('yxyxy*x*yx*yxy*x*'), convert('y*y*y*x*yxyyx*y*y*x')]
example14 = [convert('yyxyx*y*xxy*x*y*x*'), convert('y*y*y*x*yxyyx*y*y*x') ]
example15 = [convert('yyyxyx*y*y*xxy*x*y*x*'), convert('y*y*y*x*yxyyx*y*y*x')]
exampleMannan = [convert('x*x*yxxy*'), convert('y*y*y*x*yxyyx*y*y*x')] # works, obviously
