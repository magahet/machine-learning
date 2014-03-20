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
public class MultiTest {
    /** The n value */
    private static int N = 8;
    private static int maxInt = (int) Math.pow(2, N);

    private double maxValue(EvaluationFunction ef) {
        double maxVal = 0.0;
        double curVal;
        for (int i = 0; i < maxInt; i++) {
            curVal = ef.value(intToBitString(i));
            if (curVal > maxVal) {
                maxVal = curVal;
            }
        }
        return maxVal;
    }

    private double[] getAllValues(EvaluationFunction ef) {
        double[] values = new double[maxInt];
        for (int i = 0; i < maxInt; i++) {
            values[i] = ef.value(intToBitString(i));
        }
        return values;
    }

    private Instance intToBitString(int x) {
        double[] digits = new double[N];
        for (int j = 0; j < N; ++j) {
            digits[N-j-1] = x & 0x1;
            x >>= 1;
        }
        return new Instance(digits);
    }
    
    public static void main(String[] args) {
        int evalChoice = Integer.parseInt(args[0]);
        int oaChoice = Integer.parseInt(args[1]);

        EvaluationFunction[] ef = new EvaluationFunction[4];
        ef[0] = new IntEvaluationFunction();
        ef[1] = new CountOnesEvaluationFunction();
        ef[2] = new FourPeaksEvaluationFunction(N/10);
        ef[3] = new FlipFlopEvaluationFunction();


        //int[] ranges = new int[N];
        //Arrays.fill(ranges, 2);
        //Distribution odd = new DiscreteUniformDistribution(ranges);
        //NeighborFunction nf = new DiscreteChangeOneNeighbor(ranges);
        //MutationFunction mf = new DiscreteChangeOneMutation(ranges);
        //CrossoverFunction cf = new UniformCrossOver();
        //Distribution df = new DiscreteDependencyTree(.1, ranges); 
        //HillClimbingProblem hcp = new GenericHillClimbingProblem(ef, odd, nf);
        //GeneticAlgorithmProblem gap = new GenericGeneticAlgorithmProblem(ef, odd, mf, cf);
        //ProbabilisticOptimizationProblem pop = new GenericProbabilisticOptimizationProblem(ef, odd, df);
        
        //RandomizedHillClimbing rhc = new RandomizedHillClimbing(hcp);      
        //FixedIterationTrainer fit = new FixedIterationTrainer(rhc, 200);
        //int iterations = 200;
        //for (int i = 0; i < iterations; i++) {
            //rhc.train();
            //System.out.println(ef.value(rhc.getOptimal()));
        //}
        
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
