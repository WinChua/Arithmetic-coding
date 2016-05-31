class Parse(object):
    def __init__(self, charset):
        self.charset = list(charset)
        self.length = len(charset)
        self.initPro = [1.0/self.length  for i in self.charset]      
        self.initDiv = self.getDiv((0, 1), self.initPro)

    def getDiv(self, Div, Pro):
        medianPro = map(lambda x: x *(Div[1] - Div[0]), Pro)
        currentDiv = reduce(lambda x, y:x + [x[-1] + y], medianPro[1:],medianPro[:1])
        currentDiv = map(lambda x:  x + Div[0], currentDiv)
        currentDiv = zip([Div[0]] + currentDiv[:-1], currentDiv)
        return currentDiv

    def init(self):
        self.curLen = self.length
        self.curPro = self.initPro
        self.curDiv = self.initDiv
        self.targetDiv = (0,1)
    
    def update(self, char):
        '''
            when get a char
            update length, pro, div
        '''
        
        self.curPro = map(lambda x: x * self.curLen, self.curPro)
        self.curPro[self.charset.index(char)] += 1
        self.curLen += 1
        self.curPro = map(lambda x: x / self.curLen, self.curPro)
        self.targetDiv = self.curDiv[self.charset.index(char)]
        self.curDiv = self.getDiv(self.targetDiv, self.curPro)
        
        

    def encode(self, string):
        self.init()
        for char in string:
            self.update(char)

        return sum(self.targetDiv)/2, self.curLen - self.length

    def decode(self, tar, length):
        self.init()
        ori = []
        for i in range(length):
            for j in range(len(self.charset)):
                if tar < self.curDiv[j][1] and \
                    tar >= self.curDiv[j][0]:
                    ori.append(self.charset[j])
                    break
            self.update(self.charset[j])
        return "".join(ori)
                    
                
            
        





        
