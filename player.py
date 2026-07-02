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
        """Initialize player with name, wallet, and a coin."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Toss the player's coin."""
        self.__coin.toss()

    def get_coin_side(self):
        """Return the side of the coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Increase wallet by 1."""
        self.__wallet += 1

    def lose_coin(self):
        """Decrease wallet by 1."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return current wallet value."""
        return self.__wallet

    def get_name(self):
        """Return player name."""
        return self.__name