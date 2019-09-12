### Due Friday 9/13 at 5pm {#h.m7tqh8z30hz2 .c1}

### Background {#h.6dgilapv53zb .c1}

The Prisoner's Dilemma is a classic problem in game theory which is
often used to explore behaviors in a situation of strategic
interdependence.

The usual presentation of the problem is that two suspects are being
interrogated separately by a detective. The detective has insufficient
evidence to make an arrest, so is depending on a plea bargain to make a
convincing case.

The detective offers each suspect the following deal: "defect," and
admit to the crime in exchange for early parole, or "cooperate" (with
the other prisoner) and refuse to admit the crime. Neither suspect is
told of the other's choice. As one might expect, if both cooperate (C,C)
(=don't admit) then both are released (for payoff of 3 each). If one
defects while the other cooperates, (D,C) or (C,D), then the person who
defects (=admits) is released and rewarded (payoff 5) while the other
serves a long sentence (payoff 0). If both defect (D,D) (=admit) then
they both go to prison but with early parole (payoff 1). We use payoffs
adjusted by +5 here relative to the presentation of the game in Chapter
2.

When played once, only one equilibrium exists: both suspects defect and
both face prison time with early parole. This is a dominant strategy
equilibrium.  However, if both suspects had cooperated, then both would
have been gone free. This is the dilemma!

When played once, the prisoners make their choices confident in the
knowledge that their opponent would never know of a betrayal. In the
iterated prisoner's dilemma (IPD), the game is repeated, and the
suspects can make their decisions based on knowledge of previous
betrayals. Cooperation can occur in this version of the game because a
player is able to punish a treacherous opponent.

In his 1984 book The Evolution of Cooperation, Robert Axelrod describes
the results of a tournament he organized for academics to submit IPD
strategies for a fixed number of rounds. The winner was the strategy
"tit for tat" ---play the same move as was chosen by the opponent in the
previous round.

In general, Axelrod found that altruistic strategies triumphed over
greedy ones. At the 20th anniversary of the competition, a new strategy
from University of Southampton, UK outperformed even tit-for-tat. U.
Southampton made multiple entries into the competition. At each game, an
entry would recognize if its opponent was another U. Southampton entry
or an enemy. Some of the entries were self-sacrificing, continuously
cooperating to another U. Southampton entry (which would defect),
allowing those entries to take the top rankings. If a U. Southampton
entry did not recognize its opponent as one of its own, it would
continuously defect to minimize its opponent's score. Interestingly
enough, Richard Dawkins had already predicted the success of such a
strategy in his book The Selfish Gene.

For more information on the Prisoner's Dilemma (and the iterated
prisoner's dilemma), you can check out the [Wikipedia
article.](https://www.google.com/url?q=https://en.wikipedia.org/wiki/Prisoner%2527s_dilemma%23The_iterated_prisoner.27s_dilemma&sa=D&ust=1568304790370000) 

For this problem set, you will create a submission to an IPD tournament
that is similar to the one Axelrod set up in 1984 but with a twist.

In particular, the information your player receives about its opponent's
previous action is noisy, and with probability 0.05 your player receives
incorrect information about the previous action of the other player.
(Note: the payoffs are for the correct action, but you don't learn the
payoff.) The tit-for-tat strategy is not reliable in noisy environments.
To understand why, imagine that Alice is told that her opponent Bob
defected, when in fact Bob cooperated. Alice would then defect, falsely
punishing Bob, and the mistaken defections will echo until someone gets
the wrong information once again. What do you think would be the best
strategy to overcome a noisy environment for IPD? In discussing the
complications that noise adds to his tournament, Axelrod said that
"Noise calls for forgiveness, but too much forgiveness invites
exploitation." How will you design a winning agent for such an
environment?

### Announcements {#h.6hmd4j14b49u .c1}

-   Grading: You will get full credit for your agent just by submitting
    an agent. In addition, your explanation will be graded on a scale of
    0, 1, 2 -- where 0 is an unsatisfactory explanation, 1 is a mediocre
    explanation, and 2 is a well written explanation. We only expect a
    maximum two paragraphs of explanation altogether. In addition, there
    will be a small bonus for agents that perform well in the class
    tournament.
-   Collaboration policy: While you are permitted to discuss your agent
    designs with each other as much as you like, you must submit your
    own agent and explanation for that agent (submission instructions
    below).

* * * * *

###  {#h.sc5mf3x1mqq .c1 .c17}

### Part 1: Making your Agents: {#h.4w1wn1436n4e .c1}

#### The game: {#h.c2jnmakjsd3r .c15}

Your task is to create an agent for the iterated noisy prisoner's
dilemma described above. In each round, there will be a 5% probability
of mis-detecting your opponent's move. The scores for each round are as
follows.

+--------------------------+--------------------------+--------------------------+
|                          | C                        | D                        |
+--------------------------+--------------------------+--------------------------+
| C                        | 3,3                      | 0,5                      |
+--------------------------+--------------------------+--------------------------+
| D                        | 5,0                      | 1,1                      |
+--------------------------+--------------------------+--------------------------+

This means that:

-   If both players cooperate (CC) then both get a score of 3.
-   If player \#1 defects, but player \#2 cooperates (DC) then player
    \#1 gets a score of 5, while player \#2 gets a score of 0.
-   If player \#1 cooperates, but player \#2 defects (CD) then player
    \#1 gets a score of 0, while player \#2 gets a score of 5.
-   If both players defect (DD) then both players get a score of 1.

The scores are computed using the actual joint action of the two agents,
even if the 5% noise leads one or both agents to get the wrong
information about the other's action.

#### Planning: {#h.lofi33m5543q .c15}

You will be modeling a game strategy using an automaton machine,
following the description in Chapter 4. The difference is that your
machines can specify a probability of action C in each state, and need
not just emit an action deterministically. Along with the probability of
cooperating in a state, your machine will specify the transition to a
new state, based on the observed joint action, which may have a mistaken
observation of the other player's action, as described above. Of course
the observation of your own action is always correct.

To make this clearer, here are a few examples, which also introduce the
way you'll specify your agents. The first is a simple automaton that has
one state, and thus always stays in it. This would look something like
this:

0: 0.4 0 0 0 0

The first number represents the index of the current state, the second
number the probability of cooperation in the state, and the last four
numbers represent transitions to make in response to whether you and
your opponent defect or cooperate (explained in more detail in the next
section). In this case, there is only one state, so the transitions all
have to remain in the same state and the only interesting part of the
design is the probability of cooperation, which is 0.4 in this case.

A slightly more complicated automaton might have two states with
different probabilities of cooperation, and switch between them based on
what the opponent does. It might look something like this:

0: 0.6 1 0 0 1

1: 0.8 1 0 0 1

There are two states (0 is always the initial state). When in state 0,
the automaton will cooperate with probability 0.6 and in two situations
(if both players cooperated or both players defected -- explained in
more detail below) it will move to state 1. When in state 1, it will
cooperate with probability 0.8 and will return to state 0 if the players
acted differently (one defected and one cooperated).

In this assignment, you can have between 1 and 5 states, (where state 0
will always be the initial state, and the subsequent states are numbered
1, 2, 3 and 4). Your goal is to define probabilities and transitions for
each of the states in the format below. You need not use all 5 states.

#### Format: {#h.86xcsd6avnn2 .c15}

Each agent should have the following format. This agent is composed of
three states, so it is written on three lines.

Your agent should have between 1 and 5 lines of text for 5 maximum
states.

0: 0.1 1 0 0 1

1: 0.7 1 1 0 2

2: 0.4 2 2 1 0

Each line has format: state\_id: prob\_of\_cooperate state\_on\_cc
state\_on\_cd state\_on\_dc state\_on\_dd Where:

-   state\_id is the id of the state. These must be 0,1,2,3,4 in that
    order.
-   prob\_of\_cooperate is the probability of cooperating when in this
    state (and thus one minus this value is the probability of
    defecting).
-   state\_on\_cc is the state to move to on information that both
    agents cooperated in this round.
-   state\_on\_cd is the state to move to on information that your agent
    cooperated and the other agent defected in this round.
-   state\_on\_dc is the state to move to on information that your agent
    defected and the other agent cooperated in this round.
-   state\_on\_dd is the state to move to on information that both
    agents defected in this round.Remember that your automata gets noisy
    information about the play of the other agent. With probability
    0.05, the transition will be based on the wrong information about
    the other agent's action.

#### Testing: {#h.65zwd0zczp2j .c15}

We have provided a mechanism to test your agents. Using [this
page](https://www.google.com/url?q=http://cs136-hw0.seas.harvard.edu/compete.php&sa=D&ust=1568304790384000) you
can enter two agents and run a simulation for a specified number of
rounds. The agents must be entered in the above format. The simulation
result reports the round number, what action was taken by the two
agents, what actions were observed (because the data is noisy this may
be different than the actual actions taken), the score after the round,
and what states were moved to at the end of the round.

### Part 2: Analysis: {#h.5z7k0wmckel7 .c1}

Write a short write-up -- two paragraphs maximum -- explaining how your
agent works and why you designed it that way. How do you think it will
do against the agents of the other students?

### Part 3: Submission: {#h.7jg96o44uup5 .c1}

By Friday 9/13, 5p, use the form
[here](https://www.google.com/url?q=https://docs.google.com/forms/d/e/1FAIpQLSfTIdSFyR_6nPCtW3SczmfcoR0guNiU6GuIqfWmZSX_uzWXQQ/viewform?usp%3Dsf_link&sa=D&ust=1568304790386000) to
submit the assignment. There is a field for your name, Harvard username,
agent and explanation. Again, each person should submit an agent and
explanation.

### Part 4: Competition {#h.afge84f6l81e .c1}

We will run each submitted agent against each of the others 10 times,
with each game lasting 100 rounds. We will rank agents by their
cumulative score.

### Part 5: Results {#h.8lglqaq1a53b .c1}


