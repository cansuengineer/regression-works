# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:40:19 2019

@author: Cansu
"""
import numpy


#X=[14,35,22,29,6,15,17,20,12,29]
#arr = numpy.array([ 12, 11, 14, 15, 16, 17, 15, 21, 12, 14, 15, 16, 17])
X = numpy.array([ 14,35,22,29,6,15,17,20,12,29])

#arr = numpy.array([])

print(' X için normalizasyon : ')
# Get the maximum element from a Numpy array
maxElement = numpy.amax(X)
print('Max X : ', maxElement)

minElement = numpy.amin(X)
print('Min X : ', minElement)

maxeksimin = maxElement -minElement

print('bolum ', maxeksimin)
 
for value in range(0,len(X)):
    formul=(value-minElement)/(maxeksimin)
    print('deger ', formul)

Y = numpy.array([ 28,66,38,70,22,27,28,47,14,68])

#arr = numpy.array([])

print(' Y için normalizasyon : ')
# Get the maximum element from a Numpy array
maxElement = numpy.amax(Y)
print('Max Y : ', maxElement)

minElement = numpy.amin(Y)
print('Min Y : ', minElement)

maxeksimin = maxElement -minElement

print('bolum ', maxeksimin)
 
for value in range(0,len(Y)):
    formul=(value-minElement)/(maxeksimin)
    print('deger ', formul)
