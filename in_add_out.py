# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 02:43:04 2017

@author: ARSHABH SEMWAL
"""

# since constrain of addition is not using arithmetic operator bitwise operator are used
# addition of two bit is xor and the carry is and
 
def add(x ,y):
    if y==0:
        return(x)
    else :
        return(add(x^y,(x&y)<<1))
 
inp = open('in.txt' , 'r')
a = list(inp)
n = int(a[0].strip())
a = a[1:]
output = open('output.txt','w')
output.write(str(n))
d=1
for i in a:
    c=list(map(int , i.strip().split(' ')))
    x,y=c[0] ,c[1]
    s = '\n'+'#Case'+' '+str(d)+' = '+str(add(x,y))
    output.write(s)
    d+=1

output.close()
inp.close() 