from random import random
from agent import ACTION


def fuzz_result(action_profile):
    a1, a2 = action_profile
    if random() < 0.05:
        a1 = ACTION.flip(action_profile[0])

    if random() < 0.05:
        a2 = ACTION.flip(action_profile[1])

    return (a1, a2)
