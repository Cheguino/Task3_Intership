# judge.py

from outcome import Outcome

class Judge:
    def __init__(self, moves_count):
        self.moves_count = moves_count

    def decide(self, first_move, second_move):
        if first_move == second_move:
            return Outcome.DRAW

        if (second_move > first_move and second_move - first_move <= self.moves_count // 2) or \
           (second_move < first_move and first_move - second_move > self.moves_count // 2):
            return Outcome.WIN

        return Outcome.LOSE
