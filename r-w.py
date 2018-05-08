#!/bin/python36
'read /tmp/ip.txt,handle,write the result to /tmp/2.txt'
__author__="fengjf"

import os
l1=[]
def rAwfile():
    with open('/tmp/ip.txt','r') as f1:
        for eachline in f1:
            l1.append(eachline.strip())
    with open('/tmp/3.txt','w') as f2:
        for mem in l1:
            f2.write('%s%s' % (mem,os.linesep))

if __name__ == '__main__':
    rAwfile()
    


