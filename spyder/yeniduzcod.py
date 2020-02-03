# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:35:06 2019

@author: Cansu
"""

Y = [20,32,15,45]
X = [3,7,2,8]

sec=5
i=0

Ykare=0
Xkare=0

Ytoplam=0
Xtoplam=0

YcarpimX=0
Xoakt=0
Yoakt=0
YXct=0

for a in range(0,len(Y)):
    c=int( Y[a])
    Ykare +=pow(c,2)
    Xkare +=pow(int(X[a]),2)
    Ytoplam += int(Y[a])
    Xtoplam +=int(X[a])
    YcarpimX += int(X[a])*int(Y[a])
    
Yort=Ytoplam/len(Y)
Xort=Xtoplam/len(X)

Xoakt=Xkare-(len(X)*pow(Xort,2))
Yoakt=Ykare-(len(Y)*pow(Yort,2))
    
YXct=YcarpimX-(len(X)*Xort*Yort)

a=YXct/Xoakt
b=Yort-(a*Xort)

print("gelir ortalaması %d" %Xort)
print("Yiyecek harcaması %d" %Yort)

print (" Gelir'in karesi %d"  %Xkare)
print  (" yiyecek harcamasının karesi %d"%Ykare)





