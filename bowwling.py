import random


#we define class player and functions for scoring
class Player(object):
    def __init__(self, name):
        self.name = name
        self.score = [] #list of all throws
        self.framescore = [] #list of scores for each frame
        self.scorelist = []

    def newThrow(self):  #there are 2 possibilites for each throw, either score of 10 or 2 throws
        x=random.randint(0,10)
        self.score.append(x)
        remain = 10-x #remaning pins
        if x == 10: 
            self.framescore.append(x)
            self.scorelist.append([10])
        if x != 10:
            y=random.randint(0,remain) #now we can only generate from 0 to reamining pins
            self.score.append(y)
            self.framescore.append(x+y)
            self.scorelist.append([x,y])

    def lastFrameStrike(self): #if 10th frame is strike, player gets 2 new throws
        for i in range(2):
            x = random.randint(0,10)
            self.score.append(x)
            self.framescore.append(x)
            self.scorelist.append([x])

    def lastFrameSpare(self): #if 10th frame is spare, player gets one more throw
        x = random.randint(0,10)
        self.score.append(x)
        self.framescore.append(x)
        self.scorelist.append([x])


    def showScore(self):
        result=0
        if len(self.scorelist) > 10:
            scorelist1=self.scorelist[:10] #we make a copy of list with only 10 frames
        else:
            scorelist1=self.scorelist[:]
        for i in range(2):
            scorelist1.append([0]) #we append 0 to it so we avoid indexing problems in the next code
        for val, item in enumerate(self.scorelist):
            if item == [10]: #if strike
                try:
                    value = item[0]+sum(scorelist1[val+1])
           
                    if scorelist1[val+1] == [10]:
                        value = 10 + 10 +scorelist1[val+2][0]
                    result += value
                except IndexError:
                     pass
            elif sum(item) == 10: #if spare
                try:
                    value1=sum(item) + scorelist1[val+1][0]
                    result += value1
                except IndexError:
                    pass
            else: 
                value2=sum(item)
                result+=value2
        #adding score if 10th frame was strike or spare
        if (len(self.framescore)==11 and self.scorelist[8]==[10]):
            result += 2*(self.scorelist[10][0])
        elif (len(self.framescore)==12 and self.scorelist[8]==[10]):
            result += (2*(self.scorelist[10][0])+self.scorelist[11][0])#enkrat za 8 enkrat za zadnjega
        elif (len(self.framescore)==11):
            result += self.scorelist[10][0]
        elif (len(self.framescore)==12):
            result += (self.scorelist[10][0]+self.scorelist[11][0])
        print(self.scorelist)
        print(self.name+' final result is '+str(result))

        
iks=Player('John')
eks=Player('Mark')
i=0
frame=10

#run for each frame
while (i<frame):
    iks.newThrow()
    eks.newThrow()
    i +=1

#in next if statements we check results of 10th frame and give possible new throws
if (iks.score[-1]==10): 
    iks.lastFrameStrike()
elif (iks.score[-1]+iks.score[-2]==10):
    iks.lastFrameSpare()
if (eks.score[-1]==10):
    eks.lastFrameStrike()
elif (eks.score[-1]+eks.score[-2]==10):
    eks.lastFrameSpare()

print('Scores for each throw and score in each frame:')
print(iks.score)
iks.showScore()
print('============')
print('Scores for each throw and score in each frame:')
print(eks.score)
eks.showScore()
