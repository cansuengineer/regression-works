# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:35:06 2019

@author: Cansu
"""
#y bağımlı değişken , x de bağımsız değişken
X=[14,35,22,29,6,15,17,20,12,29]
Y=[28,66,38,70,22,27,28,47,14,68]


#Y = [9,15,7]
#X = [35,49,21]

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

print("Xort %d" %Xort)
print("Yort %d" %Yort)

print (" Xkarei %d"  %Xkare)
print  (" Ykare %d" %Ykare)



print(b)
print(a)


