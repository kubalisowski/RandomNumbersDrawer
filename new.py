import random

class Variables:
    file = 'numbers.txt'

class Read:
    def __init__(self, file):
        self.file = file

    def readFile(self):
        numsRead = list()
        with open(self.file) as f:
            for line in f.readlines():
                numsRead.append(line.rstrip())
            f.close()
        return numsRead

class Draw:
    def __init__(self, numsRead, file):
        self.numsRead = numsRead
        self.file = file

    def drawNum(self):
        if len(self.numsRead) is 150:
            with open(self.file, 'w') as f:
                f.close()
            return print('Wszystkie psalmy zostały wylosowane!\nZerowanie licznika')

        if len(self.numsRead) is 0:
            firstNum = random.choice(range(1,150))
            with open(self.file, 'w') as f:
                f.write(str(firstNum))
            f.close()
            return print('FIRSTWylosowany psalm: ' + str(firstNum) + '\n')
        else:
            numsFull = list()
            for n in range(1, 151):
                numsFull.append(str(n))

            numsDifference = list(set(numsFull) - set(self.numsRead))
            randNum = random.choice(numsDifference)

            self.numsRead.append(randNum)

            with open(self.file, 'w') as f:
                for n in self.numsRead:
                    f.write('%s\n' % n)
                f.close()

            return print('Wylosowany psalm: ' + str(randNum) + '\n')


Var = Variables()

ReadObj = Read(Var.file)
readVar = ReadObj.readFile()

DrawObj = Draw(readVar, Var.file)
drawVar = DrawObj.drawNum()
