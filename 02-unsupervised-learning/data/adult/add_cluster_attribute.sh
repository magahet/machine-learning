#!/bin/bash


java -cp /usr/share/java/weka.jar weka.filters.unsupervised.attribute.AddCluster \
-W "weka.clusterers.EM -N 3" \
-I last \                 # we want to ignore the class attribute
-i adult.data.arff \
-o out.arff
