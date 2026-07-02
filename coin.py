"""
Program Name: Match Coins Game - Coin Class
Author: Imran Afick
Purpose: Represents a single coin that can be tossed to show Heads or Tails.
Starter Code: None
Date: July 2, 2026
"""

import random

class Coin:
    def __init__(self):
        """Initialize coin with default side as Heads."""
        self.__sideup = "Heads"

    def toss(self):
        """Randomly set coin side to Heads or Tails."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return current side of the coin."""
        return self.__sideup