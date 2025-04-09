class Game:
    """
    Represents a game of bowling. Handles scoring with strike and spare bonuses,
    and manages special cases like the 10th frame.
    """

    def __init__(self):
        """
        Initializes the game with score and frame tracking.
        """
        self.total = 0  # Total game score
        self.frame = 1  # Current frame number (1–10)
        self.roll_in_frame = 0  # Whether it's the first or second roll in the current frame
        self.prev_pins = 0  # Pins knocked down in previous roll (used for spare detection)
        self.bonus_rolls = []  # Tracks remaining bonus rolls for strikes/spares
        self.extra_rolls = 0  # Extra rolls awarded in 10th frame due to strike/spare
        self.in_bonus = False  # True if game is in bonus roll mode (10th frame only)

    def roll(self, pins: int):
        """
        Simulates a roll in the game.

        Args:
            pins (int): The number of pins knocked down in the roll (0–10).
        """
        # Apply pending bonuses
        for i in range(len(self.bonus_rolls)):
            if self.bonus_rolls[i] > 0:
                self.total += pins
                self.bonus_rolls[i] -= 1

        # Add score from this roll
        self.total += pins

        # Handle first 9 frames
        if self.frame < 10:
            if pins == 10 and self.roll_in_frame == 0:  # Strike on first roll
                self.bonus_rolls.append(2)
                self.frame += 1
            elif self.roll_in_frame == 0:  # First roll of the frame
                self.prev_pins = pins
                self.roll_in_frame = 1
            else:  # Second roll
                if self.prev_pins + pins == 10:  # Spare
                    self.bonus_rolls.append(1)
                self.frame += 1
                self.roll_in_frame = 0
        elif self.frame == 10:
            self.handle_final_frame(pins)

    def handle_final_frame(self, pins: int):
        """
        Handles logic for the 10th frame and any bonus rolls.

        Args:
            pins (int): The number of pins knocked down in the roll.
        """
        if not self.in_bonus:
            if self.roll_in_frame == 0:
                self.prev_pins = pins
                self.roll_in_frame = 1
            elif self.roll_in_frame == 1:
                if self.prev_pins == 10 or self.prev_pins + pins == 10:
                    self.in_bonus = True
                    self.extra_rolls = 2 if self.prev_pins == 10 else 1
                self.roll_in_frame = 2
            else:
                self.extra_rolls -= 1
        else:
            self.extra_rolls -= 1

    def score(self) -> int:
        """
        Returns the total score of the game.

        Returns:
            int: The current total score.
        """
        return self.total
