import sys
import random

class Variables:
    numbers = 'numbers.txt'
    config = 'config.txt'
    confDict = ('minimal', 'maximal', 'counterStrike', 'regularText')
    error = 'Can\'t load the configuration file.\nPlease check values within config.txt'

class Config:
    def __init__(self, config, confDict, error):
        self.config = config
        self.confDict = confDict
        self.error = error

    def readConfig(self):
        confList = list()
        with open(self.config) as c:
            for line in c.readlines():
                confList.append(line.strip())
        config = dict(zip(self.confDict, confList))
        return config

class Read:
    def __init__(self, numbers):
        self.numbers = numbers

    def readnumbers(self):
        numsRead = list()
        with open(self.numbers) as f:
            for line in f.readlines():
                numsRead.append(line.rstrip())
            f.close()
        return numsRead

class Draw:
    def __init__(self, numsRead, numbers, config):
        self.numsRead = numsRead
        self.numbers = numbers
        self.config = config

    def drawNum(self):
        minimal = int(self.config['minimal'])
        maximal = int(self.config['maximal'])
        numsFull = list()

        for n in range(minimal, maximal + 1):
            numsFull.append(str(n))

        if len(self.numsRead) is len(numsFull):
            with open(self.numbers, 'w') as f:
                f.close()
            return print(self.config['counterStrike'])

        if len(self.numsRead) is 0:
            firstNum = random.choice(range(minimal, maximal + 1))
            with open(self.numbers, 'w') as f:
                f.write(str(firstNum))
            f.close()
            return print(self.config['regularText'] + ' ' + str(firstNum))
        else:
            numsDifference = list(set(numsFull) - set(self.numsRead))
            randNum = random.choice(numsDifference)

            self.numsRead.append(randNum)

            with open(self.numbers, 'w') as f:
                for n in self.numsRead:
                    f.write('%s\n' % n)
                f.close()

            return print(self.config['regularText'] + ' ' + str(randNum))


Var = Variables()

ReadObj = Read(Var.numbers)
readVar = ReadObj.readnumbers()

ConfigObj = Config(Var.config, Var.confDict, Var.error)
confVar = ConfigObj.readConfig()

DrawObj = Draw(readVar, Var.numbers, confVar)
drawVar = DrawObj.drawNum()
