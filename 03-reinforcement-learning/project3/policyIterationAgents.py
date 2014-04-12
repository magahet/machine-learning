# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

#import mdp
import util
import random

from learningAgents import ValueEstimationAgent


class PolicyIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, epsilon=0.01):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.epsilon = epsilon
        self.values = util.Counter()  # A Counter is a dict with default 0
        self.pi = dict([(s, random.choice(mdp.getPossibleActions(s))) for s in mdp.getStates() if not mdp.isTerminal(s)])
        self.iteration = 0
        self.delta = 0.0
        self.done = False

    def iterate(self):
        self.iteration += 1
        self.values = self.policyEvaluation(self.pi)
        unchanged = True
        for state in self.mdp.getStates():
            action_values = util.Counter()
            if self.mdp.isTerminal(state):
                continue
            for action in self.mdp.getPossibleActions(state):
                action_values[action] = self.computeQValueFromValues(state, action)
            a = action_values.argMax()
            if action_values[a] > self.values[state] + self.epsilon:
                self.pi[state] = a
                unchanged = False
        if unchanged:
            self.done = True

    def policyEvaluation(self, pi):
        """Return an updated utility mapping U from each state in the MDP to its
        utility, using an approximation (modified policy iteration)."""
        values = self.values.copy()
        while True:
            values_0 = values.copy()
            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    values[state] = self.mdp.getReward(state, None, None)
                else:
                    values[state] = self.computeQValueFromValues(state, pi[state])
            self.delta = max([abs(values_0[k] - values[k]) for k in values.keys()])
            #print values_0.values()
            #print values.values()
            if self.delta <= self.epsilon:
                break
        return values

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        q_value = 0
        if not self.mdp.isTerminal(state):
            for next_state, prob in self.mdp.getTransitionStatesAndProbs(state, action):
                q_value += prob * (self.mdp.getReward(state, action, next_state) + (self.discount * self.values[next_state]))
        return q_value

    def getPolicy(self, state):
        return self.pi[state] if not self.mdp.isTerminal(state) else None

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.pi[state] if not self.mdp.isTerminal(state) else None

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
