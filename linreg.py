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

from pyspark import SparkContext


def keyA(line):
	#Create a X matrix and find the X transpose. Return Xt * X
	line[0] =1.0
	#convert into float
	temp_x = np.array(line).astype('float')
	X =np.asmatrix(temp_x)
	Xt = X.transpose()
	
	return Xt * X

def keyB(line):
	#Create a X and Y matrix. Also find the X transpose. Return Xt * Y
	temp_y = np.array(line[0]).astype('float')
	Y = np.asmatrix(temp_y)
	line[0] =1.0
	#Convert into float
	temp_x = np.array(line).astype('float')
	X =np.asmatrix(temp_x)
	Xt = X.transpose()
	return Xt * Y
	

if __name__ == "__main__":
  if len(sys.argv) !=2:
    print >> sys.stderr, "Usage: linreg <datafile>"
    exit(-1)

  sc = SparkContext(appName="LinearRegression")

  # Input yx file has y_i as the first element of each line 
  # and the remaining elements constitute x_i
  yxinputFile = sc.textFile(sys.argv[1])
  yxlines = yxinputFile.map(lambda line: line.split(','))
  print yxlines
  
  #We need to calculate A. First Calculate (X * (X_Transpose)) and add them using reduceBYKey function  
  A = np.asmatrix(yxlines.map(lambda line: ("KeyA",keyA(line))).reduceByKey(lambda x1,x2: np.add(x1,x2)).map(lambda l: l[1]).collect()[0])
  print A
  
  #We need to calculate B. First Calculate (X * Y) and add them using reduceBYKey function
  B = np.asmatrix(yxlines.map(lambda line: ("KeyB",keyB(line))).reduceByKey(lambda x1,x2: np.add(x1,x2)).map(lambda l: l[1]).collect()[0])
  print B
 

  yxfirstline = yxlines.first()
  #print yxfirstline[0]," ",yxfirstline[1]
  yxlength = len(yxfirstline)
  print "yxlength: ", yxlength

  # dummy floating point array for beta to illustrate desired output format
  beta = np.zeros(yxlength, dtype=float)

  #
  # Add your code here to compute the array of 
  # linear regression coefficients beta.
  # You may also modify the above code.
  
  print "A:",A
  invA =  A.I
  print "Ainv:",invA
  #Perform A^-1 * B to calculate beta vector.
  beta = invA * B
  # print the linear regression coefficients in desired output format
  print "beta: "
  for coeff in beta:
      print coeff

  sc.stop()
