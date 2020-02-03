# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:40:19 2019

@author: Cansu
"""
import numpy

#numpy.amax(a, axis=None, out=None, keepdims=<no value>, initial=<no value>)

arr = numpy.array([ 12, 11, 14, 15, 16, 17, 15, 21, 12, 14, 15, 16, 17])


# Get the maximum element from a Numpy array
maxElement = numpy.amax(arr)
print('Max element from Numpy Array : ', maxElement)

minElement = numpy.amin(arr)
print('Max element from Numpy Array : ', minElement)

maxeksimin = maxElement -minElement

print('bolum ', maxeksimin)
 
for value in range(0,len(arr)):
    formul=(value-minElement)/(maxeksimin)

print('deger ', formul)
