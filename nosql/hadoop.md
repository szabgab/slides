# Hadoop
{id: hadoop}

## Hadoop notes
{id: hadoop-intro}

* Big Data Hadoop, Map Reduce
* HDFS (Hadoop Distributed File System) to store data on nodes.
* MapReduce to process data on the nodes.
* Files are split into 64 Mb blocks and each block is stored on a separate node.
* HDFS creates 3 copies of each block for redundancy.
* There is a namenode holding the metadata of where the files are split and duplicated.
* There can also be a stand by copy of the namenode to avoid having problem if the active namenode goes down.
* Volume, Variety, Velocity  (= Generating and recording a lot of data, in various formats very fast)



## Hadoop ecosystem
{id: hadoop-ecosystem}


(e.g. hive and pig, impala, sqoop, flume, hbase, hue, oozie, mahout)
Cloudera (CDH a distribution of all the parts)




## Hadoop commands
{id: hadoop-commands}

* hadoop fs -ls
* hadoop fs -put file.txt
* hadoop fs -get file.txt
* hadoop fs -tail file.txt
* hadoop fs -cat file.txt
* hadoop fs -mv
* hadoop fs -rm
* hadoop fs -mkdir
* hadoop jar some/long/path.java  -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input inputdir -output outputdir



## Hadoop entities
{id: hadoop-entities}

* job tracker (separate machine)
* task tracker (daemon on every node)



Hadoop streaming allows us to write our map and reduce code in any language.




## Hadoop entities
{id: hadoop-resources}

* [Intro to Hadoop and MapReduce](https://classroom.udacity.com/courses/ud617)





