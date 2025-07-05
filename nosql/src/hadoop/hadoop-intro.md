# Hadoop notes


* Big Data Hadoop, Map Reduce
* HDFS (Hadoop Distributed File System) to store data on nodes.
* MapReduce to process data on the nodes.
* Files are split into 64 Mb blocks and each block is stored on a separate node.
* HDFS creates 3 copies of each block for redundancy.
* There is a namenode holding the metadata of where the files are split and duplicated.
* There can also be a stand by copy of the namenode to avoid having problem if the active namenode goes down.
* Volume, Variety, Velocity  (= Generating and recording a lot of data, in various formats very fast)



