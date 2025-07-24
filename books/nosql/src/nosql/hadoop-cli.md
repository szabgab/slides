# Hadoop commands


* hadoop fs -put file.txt (split into 64Mb chunks replicated 3 times)
* hadoop jar some/long/path.java -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input inputdir -output outputdir
* hadoop fs -get outputdir/results.txt



