import arff
import numpy as np
import math
import collections

# Define the node class
class Node:
    def __init__(self):
        self.attributeIndex = -1
        self.children = []
        self.label = "Internal Node"

    def add_node(self, node):       
        self.children.append(node);

def printTree(node):
    print (node.label)
    [printTree(child) for child in node.children]
    print('--------------')
    
# Learner's Algorithm
def learner(attributelist, data):
    root = Node()
    should_stop = stop_criteria(attributelist, data, root)
    if should_stop != True:
        attributeId = choose_best_attribute(attributelist, data)
        root.attributeId = attributeId
        root.label = attributelist[attributeId][0]
        for attribute_value in attributelist[attributeId][1]:
            splitData = [row for row in data if row[attributeId] == attribute_value]
            newattributelist = attributelist[:attributeId] + attributelist[(attributeId + 1):]
            childNode = learner(newattributelist, splitData)
            root.add_node(childNode)
    return root

# Stop_Criteria
def stop_criteria(attributelist, data, root):
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
def entropy(attribute, data):
    result_True =  {}
    result_False = {}
    data_entropy = 0.0
    i = 0
    for entry in attributes:
        if (targetAttr == entry):
            break
        ++i
    
    for entry in data:
        if(entry[i] == True):
            if (result_True.has_key(entry[i])):
                result_True[entry[i]] += 1.0
            else:
                result_True[entry[i]]  = 1.0
        else:
            if (result_False.has_key(entry[i])):
                result_False[entry[i]] += 1.0
            else:
                result_False[entry[i]]  = 1.0
    return 0.3

#Calculates the best attribute to be chosen
def choose_best_attribute(attributelist, data):
    maxEntropy = 0
    bestAttribute = -1
    for attributeId in attributelist:
        if (entropy > maxEntropy):
            maxEntropy = entropy 
            bestAttribute = attributeId
    return 2


# Load the training data
dataset = arff.load(open('Test.arff'))
data = np.array(dataset['data'])
attributelist = dataset['attributes']

root = learner(attributelist, data)
printTree(root)