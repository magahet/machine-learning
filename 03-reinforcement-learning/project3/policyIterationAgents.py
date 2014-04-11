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
import sys

from learningAgents import ValueEstimationAgent


class PolicyIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=sys.maxint):
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
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0
        self.pi = dict([(s, random.choice(mdp.getPossibleActions(s))) for s in mdp.getStates() if not mdp.isTerminal(s)])

        iteration = 0
        while True:
            iteration += 1
            self.values = self.policyEvaluation(self.pi)
            unchanged = True
            for state in self.mdp.getStates():
                action_values = util.Counter()
                if self.mdp.isTerminal(state):
                    continue
                for action in self.mdp.getPossibleActions(state):
                    action_values[action] = self.computeQValueFromValues(state, action)
                a = action_values.argMax()
                if a != self.pi[state]:
                    self.pi[state] = a
                    unchanged = False
            if unchanged or iteration > iterations:
                break

    def policyEvaluation(self, pi, k=20):
        """Return an updated utility mapping U from each state in the MDP to its
        utility, using an approximation (modified policy iteration)."""
        values = self.values.copy()
        for i in range(k):
            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    self.mdp.getReward(state, None, None)
                else:
                    values[state] = self.computeQValueFromValues(state, pi[state])
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

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        if self.mdp.isTerminal(state):
            return None
        else:
            all_actions = self.mdp.getPossibleActions(state)
            best_action = None
            maxqvalue = float("-inf")
            for action in all_actions:
                temp = self.getQValue(state, action)
                if temp > maxqvalue:
                    best_action = action
                    maxqvalue = temp
            return best_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
