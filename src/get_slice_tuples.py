#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: anroco

In python how to get a slice of the tuple?

En python ¿como se puede obtener una seccion de la tupla?
'''

#create a tuple
tupla = (1, 5, 2, 7, 4, 9, 2, 4, 8, 3)
print(tupla)

#used tuple[start:stop] the start index is inclusive and the stop index
#is exclusive.
_slice = tupla[2:6]
print(_slice)

#if the start index isn't defined, is taken from the beginning of the tuple.
_slice = tupla[:5]
print(_slice)

#if the end index isn't defined, is taken until the end of the tuple
_slice = tupla[4:]
print(_slice)

#if neither is defined, returns the full tuple
_slice = tupla[:]
print(_slice)

#The indexes can be defined with negative values
_slice = tupla[-9:-3]
print(_slice)
