import gridworld


optParser = optparse.OptionParser()
optParser.add_option('-g', '--grid', action='store',
                     metavar="G", type='string', dest='grid', default="BookGrid",
                     help='Grid to use (case sensitive; options are BookGrid, BridgeGrid, CliffGrid, MazeGrid, default %default

n = getattr(gridworld, "get" + opts.grid)
mdp = mdpFunction()
mdp.setLivingReward(opts.livingReward)
mdp.setNoise(opts.noise)
env = gridworld.GridworldEnvironment(mdp)
a = valueIterationAgents.ValueIterationAgent(
mdp, opts.discount, opts.threshold)

