#!/usr/bin/env python


import gridworld
import valueIterationAgents
import policyIterationAgents
import qlearningAgents
import time
import matplotlib.pyplot as plt


discount = 0.9
threshold = 0.01

f, ax = plt.subplots(2, sharex=True)

vtimes = []
ptimes = []
viters = []
piters = []

r = range(3, 31)
for size in r:
    g = [[' ' for i in range(size)] for j in range(size)]
    g[0][0] = 'S'
    g[size - 1][size - 1] = size

    mdp = gridworld.Gridworld(g)
    mdp.setLivingReward(0)
    mdp.setNoise(0.2)
    env = gridworld.GridworldEnvironment(mdp)

    v = valueIterationAgents.ValueIterationAgent(mdp, discount, threshold)
    p = policyIterationAgents.PolicyIterationAgent(mdp, discount, threshold)

    gridWorldEnv = gridworld.GridworldEnvironment(mdp)
    actionFn = lambda state: mdp.getPossibleActions(state)
    q = qlearningAgents.QLearningAgent(
        alpha=0.5, epsilon=0.3, actionFn=actionFn)

    start = time.time()
    while not v.done:
        v.iterate()
    vtimes.append(time.time() - start)
    viters.append(v.iteration)

    start = time.time()
    while not p.done:
        p.iterate()
    #print 'policy', '{0:.3f}'.format(time.time() - start), p.iteration
    ptimes.append(time.time() - start)
    piters.append(p.iteration)

ax[0].plot(r, vtimes, label='value')
ax[0].plot(r, ptimes, label='policy')
handles, labels = ax[0].get_legend_handles_labels()
ax[0].legend(handles, labels, loc=2)


ax[1].plot(r, viters, label='value')
ax[1].plot(r, piters, label='policy')
handles, labels = ax[1].get_legend_handles_labels()
ax[1].legend(handles, labels, loc=2)

ax[0].set_title('time')
ax[1].set_title('iterations')

f.text(0.5, 0.95, 'planning performance', ha='center', va='center')
f.text(0.5, 0.04, 'grid size (n x n)', ha='center', va='center')
f.text(
    0.06, 0.5, 'fitness score', ha='center', va='center', rotation='vertical')
f.show()

    #i = 0
    #steps = 0
    #start = time.time()
    #while True
        #i += 1
        #steps += gridworld.runEpisode(q, env, discount, q.getAction, lambda x: None, lambda x: None, lambda: None)
    #print time.time() - start, i, steps




#optParser = optparse.OptionParser()
#optParser.add_option('-g', '--grid', action='store',
                     #metavar="G", type='string', dest='grid', default="BookGrid",
                     #help='Grid to use (case sensitive; options are BookGrid, BridgeGrid, CliffGrid, MazeGrid, default %default
