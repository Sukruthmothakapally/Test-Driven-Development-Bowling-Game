import unittest
from bowlingGame import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()
    
    def rollMany(self, n, pins):
        for _ in range(n):
            self.game.roll(pins)

    def rollSpare(self):
        self.game.roll(5)
        self.game.roll(5)

    def rollStrike(self):
        self.game.roll(10)
    
    def testGutterGame(self):
        self.rollMany(20, 0)
        self.assertEqual(self.game.score(), 0, "wrong result")
    
    def testAllOnesGame(self):
        self.rollMany(20, 1)
        self.assertEqual(self.game.score(), 20, "wrong result")

    def testOneSpare(self):
        self.rollSpare()
        self.game.roll(7)
        self.rollMany(17, 0)
        self.assertEqual(self.game.score(), 24, "wrong result")

    def testOneStrike(self):
        self.rollStrike()
        self.game.roll(6)
        self.game.roll(3)
        self.rollMany(17, 0)
        self.assertEqual(self.game.score(), 28, "wrong result")

    def testPerfectGame(self):
        self.rollMany(12, 10)
        self.assertEqual(self.game.score(), 300, "wrong result")

    def testAllSpares(self):
        self.rollMany(21, 5)
        self.assertEqual(self.game.score(), 150, "wrong result")

    def testMultipleSpares(self):
        self.rollSpare()
        self.rollMany(14, 3)
        self.rollSpare()
        self.rollSpare()
        self.game.roll(8)
        self.assertEqual(self.game.score(), 88, "wrong result")

    def testMultipleStrikes(self):
        self.rollMany(10, 4)
        self.rollStrike()
        self.rollMany(6, 3)
        self.rollStrike()
        self.game.roll(10)
        self.game.roll(10)
        self.assertEqual(self.game.score(), 104, "wrong result")

    def testRealGame(self):
        self.rollMany(6, 4)
        self.rollSpare()
        self.game.roll(9)
        self.game.roll(0)
        self.rollMany(6, 3)
        self.rollStrike()
        self.rollSpare()
        self.game.roll(10)
        self.assertEqual(self.game.score(), 110, "wrong result")

if __name__=="__main__":
    unittest.main()