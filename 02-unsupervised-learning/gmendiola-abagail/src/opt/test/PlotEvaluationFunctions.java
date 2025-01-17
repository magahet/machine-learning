package opt.test;

import java.util.Arrays;

import dist.DiscreteDependencyTree;
import dist.DiscreteUniformDistribution;
import dist.Distribution;

import opt.DiscreteChangeOneNeighbor;
import opt.EvaluationFunction;
import opt.GenericHillClimbingProblem;
import opt.HillClimbingProblem;
import opt.NeighborFunction;
import opt.RandomizedHillClimbing;
import opt.SimulatedAnnealing;
import opt.example.*;
import opt.ga.CrossoverFunction;
import opt.ga.DiscreteChangeOneMutation;
import opt.ga.GenericGeneticAlgorithmProblem;
import opt.ga.GeneticAlgorithmProblem;
import opt.ga.MutationFunction;
import opt.ga.StandardGeneticAlgorithm;
import opt.ga.UniformCrossOver;
import opt.prob.GenericProbabilisticOptimizationProblem;
import opt.prob.MIMIC;
import opt.prob.ProbabilisticOptimizationProblem;
import shared.FixedIterationTrainer;
import shared.Instance;

/**
 * 
 * @author Andrew Guillory gtg008g@mail.gatech.edu
 * @version 1.0
 */
public class PlotEvaluationFunctions {
    /** The n value */
    private static int N = 8;
    
    public static void main(String[] args) {
        int evalChoice = 0;
        if (args.length > 0) {
            try {
                evalChoice = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.err.println("Argument" + args[0] + " must be an integer.");
                System.exit(1);
            }
        }
        int maxInt = (int) Math.pow(2, N);

        EvaluationFunction[] ef = new EvaluationFunction[4];
        ef[0] = new EntropyEvaluationFunction();
        ef[1] = new CountOnesEvaluationFunction();
        ef[2] = new FourPeaksEvaluationFunction(N/10);
        ef[3] = new FlipFlopEvaluationFunction();

        for (int i = 0; i < maxInt; i++) {
            int x = i;
            double[] digits = new double[N];
            // Iterate SIZE times through that array
            for (int j = 0; j < N; ++j) {
                // mask of the lowest bit and assign it to the next-to-last
                // Don't forget to subtract one to get indicies 0..(SIZE-1)
                digits[N-j-1] = x & 0x1;
                // Shift off that bit moving the next bit into place
                x >>= 1;
            }
            //System.out.println(Arrays.toString(digits) + ", " + ef[evalChoice].value(new Instance(digits)));
            System.out.println(ef[evalChoice].value(new Instance(digits)));
        }
    }
}
