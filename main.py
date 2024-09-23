# main.py

import random
from hmac_1 import Hmac_functions
from table import Table
from judge import Judge
from utils import check_args

def main(args):
    if not check_args(args):
        return

    sec = Hmac_functions()
    table = Table(args)
    judge = Judge(len(args))

    game_finished = False

    while not game_finished:
        key = sec.generate_key()
        computer_move = random.randint(0, len(args) - 1)
        hmac_value = sec.generate_hmac(key, args[computer_move])

        print(f"HMAC: {hmac_value}")

        print("Available Moves:")
        for i, move in enumerate(args):
            print(f"{i + 1} - {move}")
        print("0 - Exit")
        print("? - Help")

        player_input = input("Enter your move: ")

        if player_input == "?":
            table.print_table()
            print("\n\n\n")
            continue

        if player_input == "0":
            game_finished = True
            continue

        try:
            player_move = int(player_input)
        except ValueError:
            print("You didn't select anything, please select one of the movements shown.")
            print("\n\n\n")
            continue

        if player_move <= 0 or player_move > len(args):
            print("Enter only one of the options shown (1, 2, 3, 0, ?)")
            print("\n\n\n")
            continue

        print(f"Your move: {args[player_move - 1]}")
        print(f"Computer move: {args[computer_move]}")

        outcome = judge.decide(computer_move, player_move - 1)
        if outcome == "WIN":
            print("You won!")
        elif outcome == "LOSE":
            print("You lost!")
        else:
            print("Draw!")

        print(f"HMAC key: {key}")
        print("\n\n\n")


if __name__ == "__main__":
    moves = ["Rock", "Paper", "Scissors"]  # Puedes modificar los movimientos
    main(moves)
