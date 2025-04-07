class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)
    
    def score(self):
        res = 0
        rollIndex = 0
        for _ in range(10):

            if self.isStrike(rollIndex):
                res+= self.strikeScore(rollIndex)
                rollIndex+=1

            elif self.isSpare(rollIndex):
                res+= self.spareScore(rollIndex)
                rollIndex+=2
            else:
                res+= self.gameScore(rollIndex)
                rollIndex+=2
        
        return res

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10
    
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    
    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex+2]
    
    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex+1] + self.rolls[rollIndex+2]
    
    def gameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex+1]