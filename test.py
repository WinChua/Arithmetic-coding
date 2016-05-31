import random
from encode import Parse


charset = "abcde"

gettest = lambda n: "".join([random.choice(charset) for i in range(n)])

for i in range(1000):
    test = gettest(30)
    assert test == p.decode(*p.encode(test))
