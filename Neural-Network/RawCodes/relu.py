import numpy as np

def relu(x):
    return max(0,x) 

def leaky_relu(x):
    return max(0.01*x,x)

if __name__=="__main__":
    data = int(input())
    result = relu(data)
    print(result)


""" Output
-3
0
--------
5
5
"""
