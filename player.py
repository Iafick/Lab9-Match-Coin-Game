"""
Program Name: Match Coins Game - Player Class
Author: Imran Afick
Purpose: Represents a player with a name, wallet, and a coin to toss.
Starter Code: None
Date: July 2, 2026
"""

from coin import Coin

class Player:
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin_side = None

    def toss_coin(self):
        import random
        self.__coin_side = random.choice(['Heads', 'Tails'])

    def get_coin_side(self):
        return self.__coin_side

    def win_coin(self):
        self.__wallet += 1

    def lose_coin(self):
        self.__wallet -= 1

    def get_wallet(self):
        return self.__wallet
