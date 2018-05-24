import math

def sigmoid(x, derivative=False):
    if derivative: return x*(1-x)
    return 1/(1+math.e**(-x))

if __name__=="__main__":
    data = int(input())
    result = sigmoid(data)
    print(result)


""" Output
10
0.9999546021312976
0
0.5
"""
