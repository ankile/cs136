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
        wcol0, wcol1, wcol2 = 4, 30, 10

        sorted_result = sorted(self.scores.items(), key=itemgetter(1), reverse=True)

        print(
            "\n",
            "#".rjust(wcol0 - 1) + " ",
            "Contestant".ljust(wcol1),
            "Score".rjust(wcol2),
        )

        print("-" * (wcol0 + wcol1 + wcol2 + 3))
        for i, result in enumerate(sorted_result, start=1):
            contestant, score = result
            print(
                str(i).rjust(wcol0) + " ",
                str(contestant).ljust(wcol1),
                str(score).rjust(wcol2),
            )

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
    p95 = ["0: 1.0 0 1 0 1", "1: 0.05 0 1 0 1"]
    p85 = ["0: 1.0 0 1 0 1", "1: 0.15 0 1 0 1"]
    p75 = ["0: 1.0 0 1 0 1", "1: 0.25 0 1 0 1"]
    tftt = ["0: 1.0 0 1 0 1", "1: 1.0 0 2 0 2", "2: 0.0 0 2 0 2"]
    tfttt = ["0: 1.0 0 1 0 1", "1: 1.0 0 2 0 2", "2: 1.0 0 3 0 3", "3: 0.0 0 3 0 3"]
    tftt95 = ["0: 1.0 0 1 0 1", "1: 0.95 0 2 0 2", "2: 0.0 0 2 0 2"]
    tftt75 = ["0: 1.0 0 1 0 1", "1: 0.75 0 2 0 2", "2: 0.0 0 2 0 2"]
    tftt50 = ["0: 1.0 0 1 0 1", "1: 0.50 0 2 0 2", "2: 0.0 0 2 0 2"]
    btftt95 = ["0: 0.95 0 1 0 1", "1: 0.95 0 2 0 2", "2: 0.0 0 2 0 2"]
    btftt90 = ["0: 0.90 0 1 0 1", "1: 0.90 0 2 0 2", "2: 0.0 0 2 0 2"]
    btftt75 = ["0: 0.75 0 1 0 1", "1: 0.75 0 2 0 2", "2: 0.0 0 2 0 2"]
    gbtftt90 = ["0: 0.90 0 1 0 1", "1: 0.90 0 2 0 2", "2: 0.1 0 2 0 2"]
    btftt90v2 = ["0: 0.90 0 1 0 1", "1: 1.0 0 2 0 2", "2: 0.0 0 2 0 2"]
    btftt90v3 = ["0: 1.0 0 1 0 1", "1: 0.9 0 2 0 2", "2: 0.0 0 2 0 2"]
    ex1 = ["0: 0.4 0 0 0 0"]
    ex2 = ["0: 0.6 1 0 0 1", "1: 0.8 1 0 0 1"]
    ex3 = ["0: 0.1 1 0 0 1", "1: 0.7 1 1 0 2", "2: 0.4 2 2 1 0"]

    agents = [
        Agent(ad, name="Always defect"),
        Agent(ad, name="Always defect2"),
        Agent(ad, name="Always defect3"),
        Agent(ad, name="Always defect4"),
        Agent(ac, name="Always cooperate"),
        Agent(tft, name="Tit for tat"),
        Agent(tft, name="Tit for tat2"),
        Agent(tft, name="Tit for tat3"),
        Agent(tft, name="Tit for tat4"),
        # Agent(tft, name="Tit for tat5"),
        # Agent(tft, name="Tit for tat6"),
        Agent(tftt, name="Tit for tat-tat"),
        Agent(tftt, name="Tit for tat-tat2"),
        Agent(tftt, name="Tit for tat-tat3"),
        Agent(tftt, name="Tit for tat-tat4"),
        Agent(tftt, name="Tit for tat-tat5"),
        Agent(tfttt, name="Tit for tat-tat-tat"),
        Agent(btftt95, name="Tit for tat-tat-95"),
        Agent(btftt90, name="Tit for tat-tat-90"),
        Agent(btftt75, name="Tit for tat-tat-75"),
        Agent(btftt90v2, name="Tit for tat-tat-90-100"),
        Agent(btftt90v3, name="Tit for tat-tat-100-90"),
        Agent(gbtftt90, name="Tit for tat-tat-90-10"),
        Agent(p95, name="0.95 tit for tat"),
        Agent(p85, name="0.85 tit for tat"),
        Agent(p75, name="0.75 tit for tat"),
        Agent(tftt95, name="0.95 tit for tat-tat"),
        Agent(tftt75, name="0.75 tit for tat-tat"),
        Agent(tftt50, name="0.50 tit for tat-tat"),
        Agent(ex1, name="Example 1"),
        Agent(ex2, name="Example 2"),
        Agent(ex3, name="Example 3"),
    ]

    c = Competition(agents)

    c.compete()
