package opt.test;

import java.util.Arrays;

import dist.DiscreteDependencyTree;
import dist.DiscreteUniformDistribution;
import dist.Distribution;

import opt.DiscreteChangeOneNeighbor;
import opt.EvaluationFunction;
import opt.OptimizationAlgorithm;
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
public class MultiTest {
    /** The n value */
    private static int N;
    private static int maxInt;

    private static double getMaxValue(EvaluationFunction ef, int efChoice) {
        double[] ranges = new double[N];
        if (efChoice == 0) {
            for (int i = 0; i < N; i++) {
                ranges[i] = i % 2;
            }
        } else if (efChoice == 1) {
            Arrays.fill(ranges, 1);
        } else if (efChoice == 2) {
            for (int i = 0; i < N; i++) {
                if (i <= (N / 10)) {
                    ranges[i] = 1;
                } else {
                    ranges[i] = 0;
                }
            }
        } else if (efChoice == 3) {
            for (int i = 0; i < N; i++) {
                ranges[i] = i % 2;
            }
        }
        Instance max = new Instance(ranges);
        return ef.value(max);
    }

    private static double[] getAllValues(EvaluationFunction ef) {
        double[] values = new double[maxInt];
        for (int i = 0; i < maxInt; i++) {
            values[i] = ef.value(intToBitString(i));
        }
        return values;
    }

    private static Instance intToBitString(int x) {
        double[] digits = new double[N];
        for (int j = 0; j < N; ++j) {
            digits[N-j-1] = x & 0x1;
            x >>= 1;
        }
        return new Instance(digits);
    }
    
    public static void main(String[] args) {
        N = Integer.parseInt(args[0]);
        int efChoice = Integer.parseInt(args[1]);
        int oaChoice = Integer.parseInt(args[2]);
        int iterations = Integer.parseInt(args[3]);


        maxInt = (int) Math.pow(2, N);

        EvaluationFunction[] ef = new EvaluationFunction[4];
        ef[0] = new EntropyEvaluationFunction();
        ef[1] = new CountOnesEvaluationFunction();
        ef[2] = new FourPeaksEvaluationFunction(N/10);
        ef[3] = new FlipFlopEvaluationFunction();

        double maxValue = getMaxValue(ef[efChoice], efChoice);

        if (oaChoice == 4) {
            System.out.println(maxValue);
            System.exit(0);
        }

        int[] ranges = new int[N];
        Arrays.fill(ranges, 2);

        Distribution odd = new DiscreteUniformDistribution(ranges);
        NeighborFunction nf = new DiscreteChangeOneNeighbor(ranges);
        MutationFunction mf = new DiscreteChangeOneMutation(ranges);
        CrossoverFunction cf = new UniformCrossOver();
        Distribution df = new DiscreteDependencyTree(.1, ranges); 

        HillClimbingProblem hcp = new GenericHillClimbingProblem(ef[efChoice], odd, nf);
        GeneticAlgorithmProblem gap = new GenericGeneticAlgorithmProblem(ef[efChoice], odd, mf, cf);
        ProbabilisticOptimizationProblem pop = new GenericProbabilisticOptimizationProblem(ef[efChoice], odd, df);

        OptimizationAlgorithm[] oa = new OptimizationAlgorithm[4];
        oa[0] = new RandomizedHillClimbing(hcp);
        //oa[1] = new SimulatedAnnealing(Math.pow(2, N), .95, hcp);
        oa[1] = new SimulatedAnnealing(100, .95, hcp);
        oa[2] = new StandardGeneticAlgorithm(100, 50, 50, gap);
        oa[3] = new MIMIC(200, 1, pop);
        
        double curVal = -1.0;
        double lastVal = -1.0;
        if (iterations == 0) {
            //System.out.println("max: " + maxValue);
            while (curVal < maxValue) {
                oa[oaChoice].train();
                curVal = ef[efChoice].value(oa[oaChoice].getOptimal());
                //if (oa[oaChoice].getEvalCount() % 1000 == 0) {
                    //System.out.println(curValue);
                //}
            }
            //System.out.println(curValue);
            System.out.println(oa[oaChoice].getEvalCount());
        } else {
            while (iterations > oa[oaChoice].getEvalCount()) {
                oa[oaChoice].train();
                curVal = ef[efChoice].value(oa[oaChoice].getOptimal());
                if (curVal != lastVal) {
                    System.out.println(oa[oaChoice].getEvalCount() + "," + curVal);
                }
                lastVal = curVal;
                if (curVal >= maxValue) {
                    break;
                }
            }
        }
        
        //SimulatedAnnealing sa = new SimulatedAnnealing(100, .95, hcp);
        //fit = new FixedIterationTrainer(sa, 200);
        //fit.train();
        //System.out.println(ef.value(sa.getOptimal()));
        
        //StandardGeneticAlgorithm ga = new StandardGeneticAlgorithm(20, 20, 0, gap);
        //fit = new FixedIterationTrainer(ga, 300);
        //fit.train();
        //System.out.println(ef.value(ga.getOptimal()));
        
        //MIMIC mimic = new MIMIC(50, 10, pop);
        //fit = new FixedIterationTrainer(mimic, 100);
        //fit.train();
        //System.out.println(ef.value(mimic.getOptimal()));
    }
}
