# utils.py

def check_args(args):
    if len(args) < 3 or len(args) % 2 == 0:
        print("Invalid options: please pass odd number of moves (3 or more).")
        return False
    if len(args) != len(set(args)):
        print("Invalid options: all moves must be distinct.")
        return False
    return True
