//Ashika Avula 800972702
//aavula@uncc.edu

I have compiled files in local_terminal and cluster_terminal. The following are the steps which i followed for execution.
-----------------------------------------------------------------------------------------------------------------------------------------------
login to cluster:
Syntax: ssh -X dsba­hadoop.uncc.edu -­l <username>
        ssh -X dsba­hadoop.uncc.edu -­l aavula

So my home directory on dsba­hadoop.uncc.edu is /users/aavula/
I have created path for storing assignment_4 files into cluster.

$ mkdir LinearRegression

Now next step is placing files from local to cluster(execute this command in local).
Syntax:  scp -v -r filepath <username>@dsba­hadoop.uncc.edu:/users/<username> .
command: scp -v -r /home/cloudera/Assignment4/* aavula@dsba-hadoop.uncc.edu:~/LinearRegression

First we have to create input path in hdfs from cluster. 
Syntax: hadoop fs -mkdir /user/<username>/input  
        hadoop fs -mkdir /user/aavula/input
My input path in cluster for hdfs is:
/user/aavula/input


Now place input file one at each time of execuion in HDFS using following command.
Syntax:   hadoop fs -put file* /user/<username>/input
Command:  hadoop fs -put /users/aavula/LinearRegression/yxlin.csv /user/aavula/input
          hadoop fs -put /users/aavula/LinearRegression/yxlin2.csv /user/aavula/input
       

We can check if the files are placed in our input hdfs location using the following command.
Command: hadoop fs -ls /user/aavula/input

for output:

Syntax:  spark-submit linreg.py <inputdatafile> 
         spark-submit /users/aavula/LinearRegression/linreg.py /user/aavula/input/yxlin.csv
-----------------------------------------------------------------------------------------------------------------------------------------------------
If we want to re-execute the program in cluster after any changes in the program, first we have to delete existing one by using following command.

[aavula@mba-i2 LinearRegression]$ rm -rf linreg.py
[aavula@mba-i2 LinearRegression]$ ls
yxlin2.csv yxlin.csv

Now execute this command in local system

[cloudera@quickstart Assignment4]$ scp -v -r ./linreg.py aavula@dsba-hadoop.uncc.edu:~/LinearRegression

Now type this command in cluster terminal
[aavula@mba-i2 LinearRegression]$ ls
linreg.py yxlin2.csv yxlin.csv
------------------------------------------------------------------------------------------------------------------------------------------------------
