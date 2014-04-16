#!/usr/bin/env python


import gridworld
#import valueIterationAgents
#import policyIterationAgents
import qlearningAgents
#import time
import matplotlib.pyplot as plt
import sys


discount = 0.9
threshold = 0.01

#f, ax = plt.subplots(2, sharex=True)
f, ax = plt.subplots()

vtimes = []
ptimes = []
viters = []
piters = []


def hd(a, b):
    return sum([1 for k in a.keys() if a[k] != b[k]])


def value_curve(mdp, alpha=0.5, epsilon=0.3, r=0, n=0.2):
    '''This returns the cumulative value curve for q-learning'''

    print {'a': alpha, 'e': epsilon, 'r': r, 'n': n}
    mdp.setLivingReward(r)
    mdp.setNoise(n)
    env = gridworld.GridworldEnvironment(mdp)
    start = mdp.getStartState()

    #v = valueIterationAgents.ValueIterationAgent(mdp, discount, threshold)
    #while not v.done:
        #v.iterate()
    #optimal_v = v.getValue(start)
    #print optimal_v

    actionFn = lambda state: mdp.getPossibleActions(state)
    q = qlearningAgents.QLearningAgent(
        alpha=alpha, epsilon=epsilon, actionFn=actionFn)

    e = 0
    x = []
    y = []
    total_steps = 0
    while total_steps <= 600000:
        if total_steps % 60000 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
        #time.sleep(1)
        e += 1
        steps = gridworld.runEpisode(
            q, env, discount, q.getAction, lambda x: None, lambda x: None, lambda: None)
        total_steps += steps
        x.append(total_steps // 1000)
        y.append(q.getValue(start))
        #print optimal_v, q.getValue(start)
    print
    return x, y


def q_experiment():
    fig, axes = plt.subplots()
    g = gridworld.getSimpleGrid(30)
    for a in range(1, 6):
        v = a * 0.2
        x, y = value_curve(g, alpha=v, r=-0.5, n=0.9)
        axes.plot(x, y, label='a={}'.format(v))
    h, l = axes.get_legend_handles_labels()
    axes.legend(h, l, loc=2)
    axes.set_ylabel('cumulative reward')
    axes.set_xlabel('steps (000s)')
    axes.set_title('cumulative rewards over time')
    fig.show()
    return fig, axes


def plot(y):
    fig, axes = plt.subplots()
    axes.plot(range(len(y)), y)
    fig.show()
    return fig, axes


f, a = q_experiment()

#r = range(3, 31)
#r = [30]
#for size in r:
    #print size
    #g = [[' ' for i in range(size)] for j in range(size)]
    #g[0][0] = 'S'
    #g[size - 1][size - 1] = size

    #mdp = gridworld.Gridworld(g)
    #mdp.setLivingReward(0)
    #mdp.setNoise(0.2)
    #env = gridworld.GridworldEnvironment(mdp)

    #v = valueIterationAgents.ValueIterationAgent(mdp, discount, threshold)
    #while not v.done:
        #v.iterate()
    #optimal_v = {s: v.getPolicy(s) for s in mdp.getStates()}

    #p = policyIterationAgents.PolicyIterationAgent(mdp, discount, threshold)
    #while not p.done:
        #p.iterate()
    #optimal_p = {s: p.getPolicy(s) for s in mdp.getStates()}

    ##gridWorldEnv = gridworld.GridworldEnvironment(mdp)
    ##actionFn = lambda state: mdp.getPossibleActions(state)
    ##q = qlearningAgents.QLearningAgent(
        ##alpha=0.5, epsilon=0.3, actionFn=actionFn)

    #p = policyIterationAgents.PolicyIterationAgent(mdp, discount, threshold)
    #r_p = []
    #t = 0.0
    #while not p.done:
        #start = time.time()
        #p.iterate()
        #t += time.time() - start
        #r_p.append((t, p.iteration, hd(p.pi, optimal_p)))

    #v = valueIterationAgents.ValueIterationAgent(mdp, discount, threshold)
    #r_v = []
    #t = 0.0
    #while not v.done:
        #start = time.time()
        #v.iterate()
        #t += time.time() - start
        #r_v.append((t, v.iteration, hd({s: v.getPolicy(s) for s in mdp.getStates()}, optimal_v)))

    #i = 0
    #steps = 0
    #hd = 1
    #start = time.time()
    #while hd > 0:
        #i += 1
        #steps += gridworld.runEpisode(q, env, discount, q.getAction, lambda x: None, lambda x: None, lambda: None)
        ##hd = sum([1 for s in mdp.getStates() if v.getPolicy(s) != q.computeActionFromQValues(s) and not mdp.isTerminal(s)])
        #vp = {s: v.getPolicy(s) for s in mdp.getStates()}
        #qp = {s: q.getPolicy(s) for s in mdp.getStates()}
        #deltas = [(vp[s], qp[s]) for s in vp.keys() if vp[s] != qp[s]]
        #print deltas
        #print time.time() - start, i, steps, hd
        #if not deltas:
            #break

    #start = time.time()
    #while not p.done:
        #p.iterate()
    ##print 'policy', '{0:.3f}'.format(time.time() - start), p.iteration
    #ptimes.append(time.time() - start)

    #v = valueIterationAgents.ValueIterationAgent(mdp, discount, threshold)
    #start = time.time()
    #while not v.done:
        #v.iterate()
    #vtimes.append(time.time() - start)
    #viters.append(v.iteration)

    #p = policyIterationAgents.PolicyIterationAgent(mdp, discount, threshold)
    #start = time.time()
    #while not p.done:
        #p.iterate()
    #ptimes.append(time.time() - start)
    #piters.append(p.iteration)


#ax.plot([t[0] for t in r_v], [t[2] for t in r_v], label='value')
#ax.plot([t[0] for t in r_p], [t[2] for t in r_p], label='policy')
#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles, labels, loc=2)
#ax.set_ylabel('hamming distance')
#ax.set_xlabel('time (sec)')
#ax.set_title('hamming distance over time (30x30 grid)')
#f.show()


#ax[0].plot(r, vtimes, label='value')
#ax[0].plot(r, ptimes, label='policy')
#handles, labels = ax[0].get_legend_handles_labels()
#ax[0].legend(handles, labels, loc=2)


#ax[1].plot(r, viters, label='value')
#ax[1].plot(r, piters, label='policy')
#handles, labels = ax[1].get_legend_handles_labels()
#ax[1].legend(handles, labels, loc=2)

#ax[0].set_ylabel('time')
#ax[1].set_ylabel('iterations')

#f.text(0.5, 0.95, 'planning performance', ha='center', va='center')
#f.text(0.5, 0.04, 'grid size (n x n)', ha='center', va='center')
##f.text(
    ##0.06, 0.5, 'fitness score', ha='center', va='center', rotation='vertical')
#f.show()





#optParser = optparse.OptionParser()
#optParser.add_option('-g', '--grid', action='store',
                     #metavar="G", type='string', dest='grid', default="BookGrid",
                     #help='Grid to use (case sensitive; options are BookGrid, BridgeGrid, CliffGrid, MazeGrid, default %default
