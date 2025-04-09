import unittest
from bowling_game import Game

class TestBowlingGame(unittest.TestCase):
    """
    Unit tests for the Bowling Game using the unittest framework.
    """

    def setUp(self):
        """
        Creates a new Game instance before each test.
        """
        self.g = Game()

    def roll_many(self, pins: int, times: int):
        """
        Rolls a given number of pins multiple times.

        Args:
            pins (int): Pins knocked down each roll.
            times (int): Number of rolls to perform.
        """
        for _ in range(times):
            self.g.roll(pins)

    def roll_spare(self):
        """
        Rolls a spare (5 + 5).
        """
        self.g.roll(5)
        self.g.roll(5)

    def roll_strike(self):
        """
        Rolls a strike (10 pins in one roll).
        """
        self.g.roll(10)

    def test_initial_score(self):
        """Score should be 0 before any rolls."""
        self.assertEqual(self.g.score(), 0)

    def test_gutter_game(self):
        """All rolls are gutter balls (0)."""
        self.roll_many(0, 20)
        self.assertEqual(self.g.score(), 0)

    def test_all_ones(self):
        """All rolls knock down 1 pin."""
        self.roll_many(1, 20)
        self.assertEqual(self.g.score(), 20)

    def test_one_spare(self):
        """One spare followed by a 3."""
        self.roll_spare()
        self.g.roll(3)
        self.roll_many(0, 17)
        self.assertEqual(self.g.score(), 16)

    def test_one_strike(self):
        """One strike followed by 3 and 4."""
        self.roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self.roll_many(0, 16)
        self.assertEqual(self.g.score(), 24)

    def test_perfect_game(self):
        """Twelve strikes."""
        self.roll_many(10, 12)
        self.assertEqual(self.g.score(), 300)

    def test_spare_in_last_frame(self):
        """Spare in final frame with bonus roll."""
        self.roll_many(0, 18)
        self.g.roll(7)
        self.g.roll(3)
        self.g.roll(5)
        self.assertEqual(self.g.score(), 15)

    def test_strike_in_last_frame(self):
        """Strike in final frame with two bonus rolls."""
        self.roll_many(0, 18)
        self.g.roll(10)
        self.g.roll(10)
        self.g.roll(10)
        self.assertEqual(self.g.score(), 30)

    def test_random_game(self):
        """Scores a realistic mid-range game."""
        rolls = [10, 9, 1, 5, 5, 7, 2, 10, 10, 10, 2, 3, 6, 4, 7]
        for pins in rolls:
            self.g.roll(pins)
        self.assertEqual(self.g.score(), 157)

    def test_two_consecutive_spares(self):
        """Two spares back-to-back and a normal roll after."""
        self.roll_spare()
        self.g.roll(5)
        self.g.roll(5)
        self.g.roll(3)
        self.roll_many(0, 15)
        self.assertEqual(self.g.score(), 31)

    def test_two_consecutive_strikes(self):
        """Two strikes followed by 5 and 3."""
        self.roll_strike()
        self.roll_strike()
        self.g.roll(5)
        self.g.roll(3)
        self.roll_many(0, 14)
        self.assertEqual(self.g.score(), 51)

if __name__ == "__main__":
    unittest.main()
