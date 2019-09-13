from enum import Enum
from random import random
from typing import Tuple

from uuid import uuid4


class ACTION:

    C = "C"
    D = "D"

    @classmethod
    def flip(cls, action):
        return cls.C if action == cls.D else cls.D


class ACTION_PROFILE:

    CC = (ACTION.C, ACTION.C)
    CD = (ACTION.C, ACTION.D)
    DC = (ACTION.D, ACTION.C)
    DD = (ACTION.D, ACTION.D)

    payouts = {CC: (3, 3), CD: (0, 5), DC: (5, 0), DD: (1, 1)}

    @classmethod
    def get_profile(cls, index):
        if index == 0:
            return cls.CC
        elif index == 1:
            return cls.CD
        elif index == 2:
            return cls.DC
        elif index == 3:
            return cls.DD
        else:
            raise IndexError

    @classmethod
    def get_payout(cls, profile: Tuple[ACTION, ACTION]):
        return cls.payouts[profile]


class State:
    def __repr__(self):
        return f"State(index={self.index}, p={self.probability})"

    def __init__(self, params):
        index, rest = params.split(": ")
        p, *transitions = rest.split()

        self.index = index
        self.probability = float(p)
        self.transitions = {
            ACTION_PROFILE.get_profile(i): state for i, state in enumerate(transitions)
        }


class Agent:
    def __repr__(self):
        return self.name

    def __init__(self, state_strings, name=None):
        self.states = [State(string) for string in state_strings]
        self.current_state = self.states[0]
        self.name = name if name else str(uuid4()).split("-")[-1]

    def get_action(self):
        return ACTION.C if random() < self.current_state.probability else ACTION.D

    def next_state(self, action_profile):
        next_state_index = self.current_state.transitions[action_profile]
        self.current_state = self.states[int(next_state_index)]

    def reset(self):
        self.current_state = self.states[0]


if __name__ == "__main__":

    s0 = ["0: 1.0 0 1 0 1", "1: 0.0 0 1 0 1"]
    s1 = ["0: 1.0 0 1 0 1", "1: 1.0 0 2 0 2", "2: 0.0 0 2 0 2"]
    tft = ["0: 1.0 0 1 0 1", "1: 0.0 0 1 0 1"]

    a0 = Agent(tft, name="Tit for tat")

    print(a0.current_state.transitions)

