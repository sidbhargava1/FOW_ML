from pyspark import since, keyword_only
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaWrapper
from pyspark.ml.param.shared import *
from pyspark.ml.common import inherit_doc


class KMeans(JavaEstimator, HasFeaturesCol, HasPredictionCol, HasMaxIter, HasTol, HasSeed,
             JavaMLWritable, JavaMLReadable):



if __name__ == '__main__':
    main()