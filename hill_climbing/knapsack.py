from sys import exit
import json
from typing import List, Tuple, Dict
import random

from .hill_climber import IHillClimberState, get_singular_value


class KnapsackHillClimberState(IHillClimberState):
    def __init__(self, items: Dict[str, Tuple[int, int]], target_value: int, capacity: int, bag: List[str]):
        # items: value first, weight second
        self.items = items
        self.target_value = target_value
        self.capacity = capacity
        self.bag = bag.copy()
        self.bag.sort()

    def id(self) -> str:
        return " ".join(self.bag)

    def items_value(self) -> int:
        value = 0
        for item in self.bag:
            value += self.items[item][0]
        return value

    def items_weight(self) -> int:
        weight = 0
        for item in self.bag:
            weight += self.items[item][1]
        return weight

    def value(self) -> List[int]:
        items_value = self.items_value()
        items_weight = self.items_weight()
        error_value = max(self.target_value - items_value, 0)
        error_weight = max(items_weight - self.capacity, 0)
        return [error_value + error_weight, -items_value, items_weight]

    def next(self) -> List['KnapsackHillClimberState']:
        next_states = []
        uncollected_items = []
        for item in self.items:
            if item not in self.bag:
                uncollected_items.append(item)
        # add item
        for item in uncollected_items:
            new_bag = self.bag.copy()
            new_bag.append(item)
            next_states.append(KnapsackHillClimberState(
                self.items, self.target_value, self.capacity, new_bag))
        # remove item
        for item in self.bag:
            new_bag = self.bag.copy()
            new_bag.remove(item)
            next_states.append(KnapsackHillClimberState(
                self.items, self.target_value, self.capacity, new_bag))
        # swap one item
        for item in self.bag:
            for item2 in uncollected_items:
                new_bag = self.bag.copy()
                new_bag.remove(item)
                new_bag.append(item2)
                next_states.append(KnapsackHillClimberState(
                    self.items, self.target_value, self.capacity, new_bag))

        return next_states

    def restart(self) -> 'KnapsackHillClimberState':
        new_bag = []
        for item in self.items:
            if random.random() < 0.5:
                new_bag.append(item)
        return KnapsackHillClimberState(self.items, self.target_value, self.capacity, new_bag)

    def print(self, verbose: bool = False) -> None:
        print("[" + " ".join(self.bag) + "]", "=",
              get_singular_value(self))
        if verbose and get_singular_value(self) != 0:
            next_states = self.next()
            for state in next_states:
                state.print(False)


def read_knapsack_input(filename: str) -> Dict:
    """
    JSON file format:
    {
      "T": 20,
      "M": 10,
      "Start": ["A", "E"],
      "Items": [
        {"name": "A", "V": 10, "W": 8},
        {"name": "B", "V": 8, "W": 4},
        {"name": "C", "V": 7, "W": 3},
        {"name": "D", "V": 6, "W": 3},
        {"name": "E", "V": 4, "W": 1}
      ]
    }
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    if not data:
        print("Error: empty file")
        exit(1)
    if not "T" in data:
        print("Error: missing T")
        exit(1)
    target_value = int(data["T"])
    if not "M" in data:
        print("Error: missing M")
        exit(1)
    capacity = int(data["M"])
    if not "Start" in data:
        print("Error: missing Start")
        exit(1)
    start_bag = data["Start"]
    if not "Items" in data:
        print("Error: missing Items")
        exit(1)
    items = {}
    for i, item in enumerate(data["Items"]):
        if not "name" in item:
            print(f"Error: data item #{i} missing name")
            exit(1)
        if not "V" in item:
            print(f"Error: data item #{i} missing V")
            exit(1)
        if not "W" in item:
            print(f"Error: data item #{i} missing W")
            exit(1)
        items[item["name"]] = (int(item["V"]), int(item["W"]))
    return {
        "items": items,
        "target_value": target_value,
        "capacity": capacity,
        "start_bag": start_bag
    }
