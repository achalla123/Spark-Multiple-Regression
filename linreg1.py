import sys
import numpy as np
from pyspark import SparkContext


if __name__ == "__main__":
  if len(sys.argv) !=4:  
    print >> sys.stderr, "Usage: linreg1 <datafile>"
    exit(-1)

  sc = SparkContext(appName="LinearRegression with Gradient Descent")
  
  def createX(line):
	line[0] = 1.0
	temp_x = np.array(line).astype('float')
	X = temp_x.transpose()		
	return X
  
  def computeBeta(beta,alpha,X,Xt,Y):
	 #B = B + A Xt(Y-XB)
	  XB = X * beta
	  Y_XB = np.subtract(Y,XB)
	  C = Xt * Y_XB
	  product = alpha * C
	  beta = np.add(beta,product)
	  return beta
  
  
  # The main program begins here.  
  # Input yx file has y_i as the first element of each line and the remaining elements constitute x_i
  yxinputFile = sc.textFile(sys.argv[1]) 
  # alpha is passed as 3rd argument by user in command line
  alpha = float(sys.argv[2])
  # no of Iteration is passed as 4th argument by user in command line
  noOfIterations = int(sys.argv[3])
  
  #split CSV file on the comma separator to fetch individual lines from the file
  yxlines = yxinputFile.map(lambda line: line.split(','))  
  yxfirstline = yxlines.first()
  yxlength = len(yxfirstline)
  
  beta = np.array([0])
  for i in range(1,yxlength):
	beta = np.array([beta,[0]])
  
  betaMatrix = np.asmatrix(beta)
  
  y_i = yxlines.map(lambda line: float(line[0]))
  x_i = yxlines.map(lambda line: createX(line))
  
  matrixYT = np.matrix(y_i.collect())
  matrixY = matrixYT.transpose()
  matrixX = np.matrix(x_i.collect())
  matrixXT = matrixX.transpose()
  
  for j in range(1,noOfIterations):
	betaVector = computeBeta(betaMatrix,alpha,matrixX,matrixXT,matrixY)
	
  print "Alpha:",alpha
  print "No of iterations:",noOfIterations
  print "Matrix Y:",matrixY
  print "Matrix X:",matrixX
  print "Beta:",betaVector