package shared;

import java.io.File;

import shared.DataSet;
import shared.DataSetDescription;
import shared.reader.ArffDataSetReader;
import shared.reader.CSVDataSetReader;
import shared.reader.DataSetReader;
import shared.filt.IndependentComponentAnalysis;
import shared.reader.DataSetLabelBinarySeperator;

/**
 * A data set reader
 * @author Andrew Guillory gtg008g@mail.gatech.edu
 * @version 1.0
 */
public class ICAFilter{
    /**
     * The test main
     * @param args ignored parameters
     */
    public static void main(String[] args) throws Exception {
        //DataSetReader dsr = new ArffDataSetReader("/home/gar/ml/assignments/02-unsupervised-learning/data/adult/adult.data.arff");
        DataSetReader dsr = new CSVDataSetReader(args[0]);

        //DataSetReader dsr = new ArffDataSetReader(args[0]);
        //System.out.println(ds);
        // read in the raw data
        DataSet ds = dsr.read();
        // split out the label
        IndependentComponentAnalysis filter = new IndependentComponentAnalysis(ds, 1);
        filter.filter(ds);

        System.out.println(ds);
        //System.out.println(new DataSetDescription(ds));
    }
}
