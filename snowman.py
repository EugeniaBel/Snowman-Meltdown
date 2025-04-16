from game_logic import play_game

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break
