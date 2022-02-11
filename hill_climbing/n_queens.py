from typing import List
import random

from .hill_climber import IHillClimberState


class NQueensHillClimberState(IHillClimberState):
    def __init__(self, size: int, board: List[int] = None):
        self.size = size
        if board is None:
            self.board = [i for i in range(size)]
        else:
            if len(board) != size:
                raise ValueError(
                    "Board size must be equal to the size of the board")
            self.board = board

    def id(self) -> str:
        return " ".join(str(i) for i in self.board)

    def value(self) -> int:
        return self.count_attacks()

    def count_attacks(self) -> int:
        count = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.board[i] == self.board[j] or abs(self.board[i] - self.board[j]) == abs(i - j):
                    count += 1
        return count

    def next(self) -> List['NQueensHillClimberState']:
        next_states = []
        for i in range(self.size):
            for j in range(i + 1, self.size):
                new_board = self.board.copy()
                new_board[i], new_board[j] = new_board[j], new_board[i]
                next_states.append(
                    NQueensHillClimberState(self.size, new_board))
        return next_states

    def restart(self) -> 'NQueensHillClimberState':
        new_board = [i for i in range(self.size)]
        random.shuffle(new_board)
        return NQueensHillClimberState(self.size, new_board)

    def print(self, verbose: bool = False) -> None:
        board_num_str_list = [str(i) for i in self.board]
        print("[" + " ".join(board_num_str_list) + "]", "=", self.value())
        if verbose and self.value() != 0:
            next_states = self.next()
            for state in next_states:
                state.print(False)
