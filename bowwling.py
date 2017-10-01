import random


#we define class player and functions for scoring
class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = [] #list of all throws
        self.framescore=[] #list of scores for each frame

    def newThrow(self):  #there are 2 possibilites for each throw, either score of 10 or 2 throws
        x=random.randint(0,10)
        self.score.append(x)
        remain = 10-x
        if x == 10:
            self.framescore.append(x)
        if x != 10:
            y=random.randint(0,remain)
            self.score.append(y)
            self.framescore.append(x+y)

    def lastFrameStrike(self): #if 10th frame is strike, player gets 2 new throws
        for i in range(2):
            x = random.randint(0,10)
            self.score.append(x)
            self.framescore.append(x)

    def lastFrameSpare(self): #if 10th frame is spare, player gets one more throw
        x = random.randint(0,10)
        self.score.append(x)
        self.framescore.append(x)



iks=Player('joze')
eks=Player('vladimir')
i=0
frame=10

while (i<frame):
    iks.newThrow()
    eks.newThrow()
    #in next if statements we check results of 10th frame and give possible new throws
    if (i==9) and (iks.score[-1]==10): 
        iks.lastFrameStrike()
    if (i==9) and (iks.score[-1]+iks.score[-2]==10):
        iks.lastFrameSpare()
    if (i==9) and (eks.score[-1]==10):
        eks.lastFrameStrike()
    if (i==9) and (eks.score[-1]+eks.score[-2]==10):
        eks.lastFrameSpare()
    i +=1
print(iks.name,iks.score[-5:],iks.framescore,len(iks.framescore))
print(eks.name,eks.score[-5:],eks.framescore,len(eks.framescore))
