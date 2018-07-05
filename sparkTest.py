import findspark
import os
findspark.init()

import pyspark
try:
    sc = pyspark.SparkContext()
except:
    pass
lines = sc.textFile("C:/spark/README.md")
lines_nonempty = lines.filter( lambda x: len(x) > 0 )
lines_nonempty.count()
