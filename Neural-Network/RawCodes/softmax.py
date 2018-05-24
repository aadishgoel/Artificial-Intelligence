import numpy as np

def softmax(data):
    data = np.array(data, dtype="float32")
    data = np.exp(data)/np.sum(np.exp(data))
    return data

if __name__=="__main__":
    data = list(map(int, input().split()))
    result = softmax(data)
    print(result)


""" Output
5 2 -1 3
[0.8420336  0.04192238 0.00208719 0.11395685]
"""
