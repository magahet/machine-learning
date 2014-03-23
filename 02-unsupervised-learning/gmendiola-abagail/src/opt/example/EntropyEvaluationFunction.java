package opt.example;

import util.linalg.Vector;
import opt.EvaluationFunction;
import shared.Instance;

/**
 * A function that counts the ones in the data
 * @author Andrew Guillory gtg008g@mail.gatech.edu
 * @version 1.0
 */
public class EntropyEvaluationFunction implements EvaluationFunction {
    /**
     * @see opt.EvaluationFunction#value(opt.OptimizationData)
     */
    public double value(Instance d) {
        Vector data = d.getData();
        int onesCount = 0;
        for (int i = 0; i < data.size(); i++) {
            if (data.get(i) == 1) {
                onesCount++;
            }
        }
        double total = data.size();
        double p = (onesCount / total);
        if (p == 1) {
            return 0.0;
        }
        //System.out.println(onesCount);
        //System.out.println(total);
        //System.out.println(p);
        double e = 0.0;
        e -= p * (Math.log(p) / Math.log(2));
        e -= (1 - p) * (Math.log(1 - p) / Math.log(2));
        //System.out.println(e);
        return e;
    }
}
