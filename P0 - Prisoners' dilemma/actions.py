from typing import Tuple


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

