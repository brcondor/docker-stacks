def initSpark(g,conf='local[*]'):
    if 'sc' not in g:
        try:
            import os
            os.environ['PYSPARK_PYTHON'] = 'python2'
            import pyspark
            sc = pyspark.SparkContext(conf)
            rdd = sc.parallelize(range(1000))
            rdd.takeSample(False, 5)
            print "You have configured spark properly"
            return sc
        except Exception:
            print "There is some issues with your Spark configuration"
    else:
        print "You have already created a Spark Context"

    return g['sc']

def initDf(sc):
    from pyspark.sql import SQLContext
    sqlContext = SQLContext(sc)
    return sqlContext