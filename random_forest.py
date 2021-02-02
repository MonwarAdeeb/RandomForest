import numpy
import pandas
import random
from decisionTree import buildDecisionTree, decisionTreePredictions


def trainTestSplit(dataFrame, testSize):
    if isinstance(testSize, float):
        testSize = round(testSize * len(dataFrame))
    indices = dataFrame.index.tolist()
    testIndices = random.sample(population=indices, k=testSize)
    dataFrameTest = dataFrame.loc[testIndices]
    dataFrameTrain = dataFrame.drop(testIndices)
    return dataFrameTrain, dataFrameTest


def bootstrapSample(dataFrame, bootstrapSize):
    randomIndices = numpy.random.randint(
        low=0, high=len(dataFrame), size=bootstrapSize)
    return dataFrame.iloc[randomIndices]


def createRandomForest(dataFrame, bootstrapSize, randomAttributes, randomSplits, forestSize=20, treeMaxDepth=1000):
    forest = []
    for i in range(forestSize):
        bootstrappedDataFrame = bootstrapSample(dataFrame, bootstrapSize)
        decisionTree = buildDecisionTree(
            bootstrappedDataFrame, maxDepth=treeMaxDepth, randomAttributes=randomAttributes, randomSplits=randomSplits)
        forest.append(decisionTree)
    return forest
