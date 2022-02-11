from typing import List, Protocol, Union


class IHillClimberState(Protocol):
    restarted: bool = False

    def value(self) -> Union[int, List[int]]:
        # return the value of the state
        pass

    def next(self) -> List['IHillClimberState']:
        # return a list of next states
        pass

    def restart(self) -> 'IHillClimberState':
        # return a random start state
        pass

    def print(self, verbose: bool = False) -> None:
        # print the state
        pass


class HillClimberSolver:
    def __init__(self, start_state: IHillClimberState, sideways_limit: int = 0, restarts: int = 0):
        self.sideways_limit = sideways_limit
        self.sideways = sideways_limit
        self.restarts = restarts
        self.state = start_state

    def step(self) -> bool:
        next_states = self.state.next()
        next_states.sort(key=lambda x: x.value())
        if len(next_states) == 0:
            return False
        candidate_state = next_states[0]
        if get_singular_value(candidate_state) < get_singular_value(self.state):
            self.state = candidate_state
            self.sideways = self.sideways_limit
        elif self.sideways > 0 and get_singular_value(self.state) == get_singular_value(candidate_state):
            self.state = candidate_state
            self.sideways -= 1
        elif self.restarts > 0:
            self.state = self.state.restart()
            self.state.restarted = True
            self.sideways = self.sideways_limit
            self.restarts -= 1
        else:
            return False
        return True

    def solve(self, print_states: bool = True, verbose: bool = False) -> Union['IHillClimberState', None]:
        if print_states:
            print("Start: ", end="")
            self.state.print(verbose)
        while True:
            if get_singular_value(self.state) <= 0:
                if print_states:
                    print("Goal: ", end="")
                    self.state.print(False)
                return self.state
            if not self.step():
                if print_states:
                    print("Not found")
                return None
            if print_states:
                if self.state.restarted:
                    print("restarting with: ", end="")
                else:
                    print("choose: ", end="")
                self.state.print(verbose)


def get_singular_value(state: IHillClimberState) -> int:
    if type(state.value()) == int:
        return state.value()
    else:
        return state.value()[0]
