import random
import pandas
import time
from randomForest import trainTestSplit, createRandomForest, randomForestPredictions, calculateAccuracy

dataFrame = pandas.read_csv("dataset_files/car_evaluation.csv")

buyingMapping = {"low": 1, "med": 2, "high": 3, "vhigh": 4}
dataFrame["buying"] = dataFrame["buying"].map(buyingMapping)

maintMapping = {"low": 1, "med": 2, "high": 3, "vhigh": 4}
dataFrame["maint"] = dataFrame["maint"].map(maintMapping)

doorsMapping = {"2": 2, "3": 3, "4": 4, "5more": 5}
dataFrame["doors"] = dataFrame["doors"].map(doorsMapping)

personsMapping = {"2": 2, "4": 4, "more": 6}
dataFrame["persons"] = dataFrame["persons"].map(personsMapping)

lugBootMapping = {"small": 1, "med": 2, "big": 3}
dataFrame["lug_boot"] = dataFrame["lug_boot"].map(lugBootMapping)

safetyMapping = {"low": 1, "med": 2, "high": 3}
dataFrame["safety"] = dataFrame["safety"].map(safetyMapping)

dataFrameTrain, dataFrameTest = trainTestSplit(dataFrame, testSize=0.3)

print("Random Forest - Car Evaluation Dataset")
print("  Maximum bootstrap size (n) is {}".format(dataFrameTrain.shape[0]))
print("  Maximum random subspace size (d) is {}".format(
    dataFrameTrain.shape[1] - 1))

print("\n  Change n, keep other parameters")

for i in range(200, dataFrameTrain.shape[0] + 1, 100):
    startTime = time.time()
    randomForest = createRandomForest(
        dataFrameTrain, bootstrapSize=i, randomAttributes=5, randomSplits=10, forestSize=10, treeMaxDepth=8)
    buildingTime = time.time() - startTime
    randomForestTestResults = randomForestPredictions(
        dataFrameTest, randomForest)
    accuracyTest = calculateAccuracy(
        randomForestTestResults, dataFrameTest.iloc[:, -1]) * 100
    randomForestTrainResults = randomForestPredictions(
        dataFrameTrain, randomForest)
    accuracyTrain = calculateAccuracy(
        randomForestTrainResults, dataFrameTrain.iloc[:, -1]) * 100
    print("  n = {}, d = {}, s = {}, k = {}, maxDepth = {}:".format(i, 5, 10, 10, 8))
    print("    accTest = {0:.2f}%, ".format(accuracyTest), end="")
    print("accTrain = {0:.2f}%, ".format(accuracyTrain), end="")
    print("buildTime = {0:.2f}s".format(buildingTime), end="\n")

print("\n  Change d, keep other parameters")
