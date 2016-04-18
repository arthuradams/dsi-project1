# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:42:25 2016

@author: arthuradams
"""

# import urllib2
import numpy as np
from numpy import mean, median, std, ptp, var
from scipy.stats import mode, skew
from scipy.optimize import curve_fit

import matplotlib
import matplotlib.pyplot as plt

def getStates( data ):
    states = []
    for row in data:
        states.append( row[0] )
    return states
    
def myStd( ):
    return
    
def getStatistics( data ):
    stats = {}
    stats["mean"] = mean(data)
    stats["median"] = median(data)
    stats["mode"] = mode(data)
    stats["var"] = var(data)    
    stats["std"] = std(data)
    stats["skew"] = skew(data)
    return stats

def buildDictionaries( data ):
    dataLists = { "Rate" : {}, "Verbal" : {}, "Math" : {} }
    for row in data:
        dataLists["Rate"][row[0]] = row[1]
        dataLists["Verbal"][row[0]] = row[2]
        dataLists["Math"][row[0]] = row[3]
    return dataLists
    
def getAxis( stateKeys, colDict ):
    axis = []
    for state in stateKeys:
        axis.append( colDict[state] )
    return axis

def listOfListsString( datadict ):
    printable = ""
    for key1 in datadict:
        for key2 in datadict[key1]:
            printable += str( key1 ) + " : " + str( key2 ) + " : " +\
                str( datadict[key1][key2] ) + "\n"
    return printable
        
   
filename = "sat_scores.csv"

#Mapping the url where the raw csv is. 
# url = "https://github.com/ga-students/DSI-DC-1/blob/master/week-01/project-01/assets/sat_scores.csv"
#Opening the URL
# response = urllib2.urlopen(url)

#Using numpy and genfromtxt to construct file from csv 
#This code for some reason omits the header, but still allows me to subset by column.
#I think it is because 1) names = True states that the first row is the header row with the column names;
#2) dtype = None detects from the 2nd row on what the data is;
#3) dtype stores each column with the name of it, and then the type of data; and I can use the column names to
# subset the columns as individual arrays.

# 4. Load the data into a list of lists
sat_csv = np.genfromtxt(filename, dtype = None, names = True, delimiter = ",")

# print dataString( sat_csv )

stateList = getStates( sat_csv )

#for dataType in sat_csv.dtype:
#    print np.result_type( dataType )

dataDict = buildDictionaries( sat_csv )

print listOfListsString( dataDict )

rateAxis = getAxis( stateList, dataDict["Rate"])
verbalAxis = getAxis( stateList, dataDict["Verbal"])
mathAxis = getAxis( stateList, dataDict["Math"])

plt.plot( rateAxis, verbalAxis, color="red" )
plt.scatter(rateAxis, verbalAxis, color="red" )
plt.xlabel("Rate")
plt.plot( rateAxis, mathAxis, color="blue" )
plt.scatter(rateAxis,mathAxis, color="blue" )
plt.ylabel("Verbal Score (Red)\nMath Score (Blue)")
plt.show()

plt.scatter(verbalAxis, mathAxis)
plt.xlabel("Verbal Score")
plt.ylabel("Math Score")
plt.show()

plt.hist(mathAxis,alpha=0.5)
plt.hist(verbalAxis,alpha=0.5)
plt.show()

plt.hist(rateAxis)
plt.show()

stats = {}
stats["Rate"] = getStatistics( rateAxis )
stats["Verbal"] = getStatistics( verbalAxis )
stats["Math"] = getStatistics( mathAxis )