# Pset 0 - Writeup

_Friday 13.09.2019 - Cambridge, MA_

## 1. The agent

The agent I have designed is a variation of the wellknown tit-for-tat (TfT) agent. See figure 1 for a representation of the agent in automaton-form:

![Automaton-representation of agent](https://github.com/ankile/cs136/blob/master/P0%20-%20Prisoners'%20dilemma/img/agent.jpeg)

There are two main things that makes this agent different from the normal TfT-variation:
1. There is an extra state which also is cooperative which is reached from the initial state by the opponent defecting.
2. There is a non-zero chance of the agent defecting even when it is in cooperate-mode.

The reasons for these choices will be discussed in the Analysis-section.

The agent given in the table-form is given below:

| State | P(C) | CC | CD | DC | DD |
|-------|------|----|----|----|----|
| 0     | 0.9  | 0  | 1  | 0  | 1  |
| 1     | 0.9  | 0  | 2  | 0  | 2  |
| 2     | 0.0  | 0  | 2  | 0  | 2  |


## 2. Analysis

### 1. The extra state

The extra state is another cooperative state that makes the agent a bit more forgiving. The first time the opponent defects our agent goes to state 1, where we once again is in a cooperative mode. If the opponent cooperates we go back to state 0, otherwise we will go to state 2, which will mean perpetually defecting until our opponent cooperates again.

It has previously been shown that the TfT-strategy is a very effective one. However, given the noise in this environment, two TfTs meeting each other would soon start to get in each others ways, just because of the noise. Therefore, I reason that if one can accept one transgression one will avoid going into defect-mode unnecessarily, but still avoid being exploited too heavily.

### 2. The defect-probability

The second deviation from the normal TfT-strategy is the introduction of the non-zero chance of defecting in cooperate-mode. In my case I found P(D) = 10% to work well. The reasoning here is that since the envionment is already noisy and agents will be observed to be defecting regardless of if they did or not, one can get away with actually defecting just a little bit, to exploit the other forgiving strategies, just enough to make a difference, but not so much that they will notice.

## 3. Empirical results
