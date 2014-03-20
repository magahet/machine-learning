package opt.example;

import util.linalg.Vector;
import opt.EvaluationFunction;
import shared.Instance;

/**
 * A function that counts the ones in the data
 * @author Andrew Guillory gtg008g@mail.gatech.edu
 * @version 1.0
 */
public class IntEvaluationFunction implements EvaluationFunction {
    /**
     * @see opt.EvaluationFunction#value(opt.OptimizationData)
     */
    public double value(Instance d) {
        Vector data = d.getData();
        char[] bitString = new char[data.size()];
        for (int i = 0; i < data.size(); i++) {
            bitString[i] = (String.valueOf(data.get(i))).charAt(0);
        }
        return Integer.parseInt(new String(bitString), 2);
    }
}
