-------------------------------------------------------------------------------------
Multiple Linear Regression in Spark
Name: Chinmay Rawool
Email id: crawool@uncc.edu
-------------------------------------------------------------------------------------

For execution of Linear Regression program:(linreg.py)

Step 1: Makee directory in hdfs
hadoop fs -mkdir /user/<username>/

Step 2:
Put the yxlin.csv, yxlin2.csv and linreg.py in the hdfs with the following command.

	hadoop fs -put /users/<username>/linreg.py /user/<username>/
	hadoop fs -put /users/<username>/yxlin.csv /user/<username>/
	hadoop fs -put /users/<username>/yxlin2.csv /user/<username>/

Step 3: 
Submit the code using the following command for input yxlin.csv:
	spark-submit linreg.py yxlin.csv > yxlin.out

Submit the code using the following command for input yxlin2.csv:
	spark-submit linreg.py yxlin2.csv > yxlin2.out

Step 4: Check the output in yxlin.out and yxlin2.out using the vim command.
	eg: vi yxlin.out or vi yxlin2.out

--------------------------------------------------------------------------------------
For execution of Gradient Descent program:(linreg.py)

Step 1: Makee directory in hdfs
hadoop fs -mkdir /user/<username>/

Step 2:
Put the yxlin.csv, yxlin2.csv and linreg1.py in the hdfs with the following command.

	hadoop fs -put /users/<username>/linreg1.py /user/<username>/
	hadoop fs -put /users/<username>/yxlin.csv /user/<username>/
	hadoop fs -put /users/<username>/yxlin2.csv /user/<username>/

Step 3: 
Submit the code using the following command for input yxlin.csv, alpha = 0.01, no of iterations:3
	spark-submit linreg1.py yxlin.csv 0.01 3> g_yxlin.out

Submit the code using the following command for input yxlin2.csv, alpha = 0.01, no of iterations:3
	spark-submit linreg1.py yxlin2.csv 0.01 3> g_yxlin2.out

Step 4: Check the output in yxlin.out and yxlin2.out using the vim command.
	eg: vi g_yxlin.out or vi g_yxlin2.out

--------------------------------------------------------------------------------------


AIzaSyDsKslS3nFfO9yIAwjxIwzlfE5ThJ2XsRA