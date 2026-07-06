from player import Player

def main():

    print("--- Coin Match Game ---\n")

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print(f"Player 1 has {player1.get_wallet()} coins.")
    print(f"Player 2 has {player2.get_wallet()} coins.\n")

    while True:

        choice = input("Do you want to toss the coins? (y/n): ").lower()

        if choice != 'y':
            break

        print("\nTossing...\n")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"Player 1 tossed {side1}")
        print(f"Player 2 tossed {side2}")

        if side1 == side2:
            print("...It's a Match! Player 1 wins a coin.")
            player1.win_coin()
            player2.lose_coin()
        else:
            print("...No Match! Player 2 wins a coin.")
            player2.win_coin()
            player1.lose_coin()

        # IMPORTANT: ONLY ONE WALLET PRINT
        print(f"\nPlayer 1 has {player1.get_wallet()} coins.")
        print(f"Player 2 has {player2.get_wallet()} coins.\n")

    print("\n--- Final Score ---")
    print(f"Player 1: {player1.get_wallet()} coins")
    print(f"Player 2: {player2.get_wallet()} coins")

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 wins the game!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()