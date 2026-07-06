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
        self.__sideup = "Heads"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup