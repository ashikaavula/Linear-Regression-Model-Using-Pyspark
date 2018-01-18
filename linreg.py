# linreg.py
#
# Standalone Python/Spark program to perform linear regression.
# Performs linear regression by computing the summation form of the
# closed form expression for the ordinary least squares estimate of beta.
# 
# TODO: Write this.
# 
# Takes the yx file as input, where on each line y is the first element 
# and the remaining elements constitute the x.
#
# Usage: spark-submit linreg.py <inputdatafile>
# Example usage: spark-submit linreg.py yxlin.csv
#
#

import sys
import numpy as np
from numpy.linalg import inv
from pyspark import SparkContext


if __name__ == "__main__":
  if len(sys.argv) !=2:
    print >> sys.stderr, "Usage: linreg <datafile>"
    exit(-1)

  sc = SparkContext(appName="LinearRegression")

  # Input yx file has y_i as the first element of each line 
  # and the remaining elements constitute x_i
  yxinputFile = sc.textFile(sys.argv[1])

  yxlines1 = yxinputFile.map(lambda line: line.split(',')[0])
  Y = np.asarray(yxlines1.collect(),dtype='float64')
  
  yxlines2 = yxinputFile.map(lambda line: line.split(',')[1:])
  X = np.asarray(yxlines2.collect(),dtype='float64')

  X_new = np.c_[np.ones((len(X),1)),X] 
  
  Xt = X_new.transpose()

  X_mat = np.asmatrix(X_new)
  Y_mat = np.asmatrix(Y)
  Xt_mat = np.asmatrix(Xt)

  Yt_mat = Y_mat.transpose()

  A = inv(np.dot(Xt_mat,X_mat))
  B = np.dot(Xt_mat,Yt_mat) 
  beta = np.dot(A,B)

  # print the linear regression coefficients in desired output format
  print "beta value is: "
  for coeff in beta:
      print coeff

  sc.stop()
