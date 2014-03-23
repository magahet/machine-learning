package opt;

import shared.Instance;

/**
 * A randomized hill climbing algorithm
 * @author Andrew Guillory gtg008g@mail.gatech.edu
 * @version 1.0
 */
public class RandomizedHillClimbing extends OptimizationAlgorithm {
    
    /**
     * The current optimization data
     */
    private Instance cur;
    
    /**
     * The current value of the data
     */
    private double curVal;

    /**
     * Count of same value
     */
    private long sameCount = 0;
    
    /**
     * Make a new randomized hill climbing
     */
    public RandomizedHillClimbing(HillClimbingProblem hcp) {
        super(hcp);
        cur = hcp.random();
        curVal = hcp.value(cur);
    }

    /**
     * @see shared.Trainer#train()
     */
    public double train() {
        HillClimbingProblem hcp = (HillClimbingProblem) getOptimizationProblem();
        Instance neigh = hcp.neighbor(cur);
        double neighVal = hcp.value(neigh);
        if (neighVal > curVal) {
            curVal = neighVal;
            cur = neigh;
            sameCount = 0;
        } else if (sameCount > cur.size()) {
            cur = hcp.random();
            curVal = hcp.value(cur);
        } else {
            sameCount++;
        }
        return curVal;
    }

    /**
     * @see opt.OptimizationAlgorithm#getOptimalData()
     */
    public Instance getOptimal() {
        return cur;
    }

}
