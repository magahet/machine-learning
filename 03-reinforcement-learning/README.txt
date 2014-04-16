Overview
========

Grid world MDPs, planning algorithms, and q-learning agents are all derived from code found here:

http://inst.eecs.berkeley.edu/~cs188/fa09/ projects/reinforcement/reinforcement.html

https://github.com/lfdepombo/CS188-PJ3


Modifications have been made to measure iterations, steps, elapsed time, and other such performance metrics. There have also been a number of changes to stopping conditions and reporting features.


experiments.py is used as a work area for setting up performance evaluation experiments and plotting results. This script is indented to be manipulated in an interactive shell.



Requirements
============

    Python 2.7
    Ipython or Python interactive console



Tutorial
========

## Run value iteration on Book Grid MDP

python gridworld.py -a value


## Run policy iteration on Discount Grid MDP

python gridworld.py -a policy -g DiscountGrid


## Run q-learning on Book Grid MDP

python gridworld.py -a q



Options
=======

python gridworld.py -h
Usage: gridworld.py [options]

Options:
  -h, --help            show this help message and exit
  -d DISCOUNT, --discount=DISCOUNT
                        Discount on future (default 0.9)
  -r R, --livingReward=R
                        Reward for living for a time step (default 0.0)
  -n P, --noise=P       How often action results in unintended direction
                        (default 0.2)
  -e E, --epsilon=E     Chance of taking a random action in q-learning
                        (default 0.3)
  -t T, --threshold=T   Threshold of minimum value change to continue
                        iterating (default 0.01)
  -l P, --learningRate=P
                        TD learning rate (default 0.5)
  -i K, --iterations=K  Number of rounds of value iteration (default none)
  -k K, --episodes=K    Number of epsiodes of the MDP to run (default 1)
  -g G, --grid=G        Grid to use (case sensitive; options are BookGrid,
                        BridgeGrid, CliffGrid, MazeGrid, default BookGrid)
  -w X, --windowSize=X  Request a window width of X pixels *per grid cell*
                        (default 100)
  -a A, --agent=A       Agent type (options are 'random', 'value', 'policy',
                        and 'q', default random)
  -c, --cli             Use text-only ASCII display
  -p, --pause           Pause GUI after each time step when running the MDP
  -q, --quiet           Skip display of any learning episodes
  -s S, --speed=S       Speed of animation, S > 1.0 is faster, 0.0 < S < 1.0
                        is slower (default 1.0)
  -m, --manual          Manually control agent
  -v, --valueSteps      Display each step of value iteration

