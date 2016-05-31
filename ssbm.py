from __future__ import division

import random


charset = {'a','t'}
l = list(charset)
testString = ''.join([random.choice(l) for i in range(4)])
length = len(charset)
initDiv = (0,1)
currentPro = [1.0/length  for i in l]
medianPro = map(lambda x: x*(initDiv[1]-initDiv[0]), currentPro)
currentDiv = reduce(lambda x, y:x + [x[-1] + y], medianPro[1:],medianPro[:1])
currentDiv = zip([initDiv[0]] + currentDiv[:-1], currentDiv)

for i in testString:
    currentPro = map(lambda x: x * length, currentPro)
    currentPro[l.index(i)] += 1
    length += 1
    currentPro = map(lambda x: x/length, currentPro)
    initDiv = currentDiv[l.index(i)]
    medianPro = map(lambda x: x*(initDiv[1]-initDiv[0]), currentPro)
    currentDiv = reduce(lambda x, y:x + [x[-1] + y], medianPro[1:],medianPro[:1])
    currentDiv = map(lambda x:  x+initDiv[0], currentDiv)
    currentDiv = zip([initDiv[0]] + currentDiv[:-1], currentDiv)

    
