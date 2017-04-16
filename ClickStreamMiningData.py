import arff
import numpy as np
import math
import collections

# Define the node class
class Node:
    def __init__(self):
        self.attributeId = -1
        self.children = {}
        self.label = "Internal Node"
        
    def addNode(self, node, attributeValue):       
        self.children[attributeValue] = node;

def printTree(node):
    print (node.label)
    [printTree(child) for child in node.children]
    print('--------------')
    
# Learner's Algorithm
def Learner(attributelist, data):
    root = Node()
    should_stop = stopCriteria(attributelist, data, root)
    if should_stop != True:
        attribute = chooseBestAttribute(attributelist, data)
        root.attributeId = attributeNameList.index(attribute[0])
        root.label = attribute[0]
        for attributeValue in attribute[1]:
            splitData = [row for row in data if row[root.attributeId] == attributeValue]
            newattributelist = [i for i in attributelist if i[0] != root.label]
            childNode = Learner(newattributelist, splitData)
            root.addNode(childNode, attributeValue)
    return root

# Stop_Criteria
def stopCriteria(attributelist, data, root):
    if(len(attributelist) == 0 or len(data)== 0):
        root.label = "Data or AttributeList is empty"
        return True
    elif all([row[len(row)-1] == 'True' for row in data]):
        root.label = "The User will visit next page"
        return True
    elif all([row[len(row)-1] == 'False' for row in data]):
        root.label = "The User will not visit next page"
        return True
    return False
   

#Calculates the entropy of the given data set for the target attribute
def entropy(attributeName, data):
    entropy = 0
    attributeIndex = attributeNameList.index(attributeName)
    truedictList = {}
    falsedictList = {}

    for row in data:
        if(row[len(attributelist)] == 'False'):
            if not row[attributeIndex] in falsedictList:
                falsedictList[row[attributeIndex]] = 1
            else:
                falsedictList[row[attributeIndex]] += 1
        else:
            if not row[attributeIndex] in truedictList:
                truedictList[row[attributeIndex]] = 1
            else:
                truedictList[row[attributeIndex]] += 1

    for value in attributelist[attributeIndex][1]:
        if value in truedictList:
            trueCount = truedictList[value]
        else:
            trueCount = 0
        if value in falsedictList:
            falseCount = falsedictList[value]
        else:
            falseCount = 0
        totalOccurence = trueCount + falseCount

        if totalOccurence==0:
            continue
        trueRatio= trueCount/totalOccurence
        falseRatio = falseCount/totalOccurence
        if trueRatio != 0:
            entropy += -trueRatio*math.log(trueRatio, 2)
        if falseRatio != 0:
            entropy += -falseRatio*math.log(falseRatio, 2)
    
    return entropy

#Calculates the best attribute to be chosen
def chooseBestAttribute(subAttributeList, data):
    minEntropy = 100000
    bestAttribute = -1
    for attribute in subAttributeList:
        e = entropy(attribute[0], data)
        if (e < minEntropy):
            minEntropy = e 
            bestAttribute = attribute
    
    return bestAttribute
    
def DecisionTreeTest():
    datatest = arff.load(open('testingD.arff'))
    dataTestArr = np.array(datatest['data'])
    attributeTest = datatest['attributes']
    node = root
    
    row  = 24212
    while(node and node.attributeId != -1):
        print(node.label)
        print(node.attributeId)
        attributeValue = dataTestArr[row][node.attributeId]
        
        print(attributeValue)
        if (attributeValue in node.children):
            node = node.children[attributeValue]
        else:
            break
    
    print(node.label) 
    print(dataTestArr[row])
    # TODO: check for equality of final response

# Load the training data
dataset = arff.load(open('training_subsetD.arff'))
data = np.array(dataset['data'])
attributelist = dataset['attributes']
attributelist.pop()

attributeNameList = [row[0] for row in attributelist]

#root = Learner(attributelist, data)
#print(data[0][root.attributeId])
#print(attributelist[207][1].index(data[0][root.attributeId]))
#DecisionTreeTest()
#printTree(root)