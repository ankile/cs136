from typing import List
from agent import Agent, ACTION_PROFILE
from helpers import fuzz_result
from operator import itemgetter


class Competition:
    def __init__(self, contestants: List[Agent]):
        self.contestants = contestants
        self.scores = {c: 0 for c in self.contestants}
        self.results = []

    def print_results(self):
        wcol1, wcol2 = 30, 10

        sorted_result = sorted(self.scores.items(), key=itemgetter(1), reverse=True)

        print("Contestant".ljust(wcol1), "Score".ljust(wcol2))
        print("-" * (wcol1 + wcol2))
        for contestant, score in sorted_result:
            print(str(contestant).ljust(wcol1), str(score).ljust(wcol2))

        print()

    def compete(self):
        for _ in range(10):
            for i, c1 in enumerate(self.contestants, start=1):
                for c2 in self.contestants[i:]:
                    c1.reset()
                    c2.reset()

                    for _ in range(100):
                        action_profile = (c1.get_action(), c2.get_action())
                        fuzzy_profile = fuzz_result(action_profile)

                        c1.next_state(fuzzy_profile)
                        c2.next_state(tuple(fuzzy_profile[::-1]))

                        payout = ACTION_PROFILE.get_payout(action_profile)

                        self.scores[c1] += payout[0]
                        self.scores[c2] += payout[1]

        self.print_results()
        self.results.append(self.scores)
        self.scores = {c: 0 for c in self.contestants}


if __name__ == "__main__":

    ac = ["0: 1.0 0 0 0 0"]
    ad = ["0: 0.0 0 0 0 0"]
    tft = ["0: 1.0 0 1 0 1", "1: 0.0 0 1 0 1"]
    ftft = ["0: 1.0 0 1 0 1", "1: 1.0 0 2 0 2", "2: 0.0 0 2 0 2"]

    agents = [
        Agent(ac, name="Always cooperate"),
        Agent(ad, name="Always defect"),
        Agent(tft, name="Tit for tat"),
        Agent(tft, name="Tit for tat2"),
        Agent(tft, name="Tit for tat3"),
        Agent(tft, name="Tit for tat4"),
        Agent(ftft, name="Forgiving tit for tat"),
    ]

    c = Competition(agents)

    c.compete()
