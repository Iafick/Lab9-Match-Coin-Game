"""
Program Name: Match Coins Game - Main Game Logic
Author: Imran Afick
Purpose: Runs the Match Coins game between two players using coin toss logic.
Starter Code: None
Date: July 2, 2026
"""

from player import Player

def main():
    print("\n--- Coin Match Game ---")

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    while True:
        print(f"\nPlayer 1 has {player1.get_wallet()} coins.")
        print(f"Player 2 has {player2.get_wallet()} coins.\n")

        choice = input("Do you want to toss the coins? (y/n): ").lower()

        if choice != 'y':
            break

        print("\nTossing...\n")

        # Toss coins
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"Player 1 tossed {side1}")
        print(f"Player 2 tossed {side2}")

        # Game logic
        if side1 == side2:
            print("...It's a Match! Player 1 wins a coin.")
            player1.win_coin()
            player2.lose_coin()
        else:
            print("...No Match! Player 2 wins a coin.")
            player2.win_coin()
            player1.lose_coin()

        print(f"\nPlayer 1 has {player1.get_wallet()} coins.")
        print(f"Player 2 has {player2.get_wallet()} coins.")

        # Optional game over condition
        if player1.get_wallet() == 0:
            print("\nPlayer 1 is out of coins. Player 2 wins the game!")
            break
        if player2.get_wallet() == 0:
            print("\nPlayer 2 is out of coins. Player 1 wins the game!")
            break

    # Final results
    print("\n--- Final Score ---")
    print(f"Player 1: {player1.get_wallet()}")
    print(f"Player 2: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 wins the game!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()