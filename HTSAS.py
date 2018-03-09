#!/usr/bin/env python3
''' 
Code by Stephane Gallet, <gallet.stephane@gmail.com>
based on "How to Share a Secret" by Adi Shamir
Published by :Communications of the ACM
November 1979, Volume 22, Num. 11
'''

import numpy as np
import random


def split_secret(secret, k, n):
    ''' 
    Secret in an integer
    k is the minimum number of keys to get the secret back
    n is the total number of keys generated
    '''
    D = []
    A = []
    B = []
    A.append(int(secret))
    for j in range(1,n):
        A.append(random.randrange(1,100))

    for i in range(1,n+1):
        B.append(A[0])
        for j in range(1,k):
            B.append(A[j]*i**j)
        D.append(sum(B))
        B = []
    
    S = {}
    for y in range(len(D)):
        S[y] = D[y]
    print('Keys:',S)
    return S

def get_secret(k,keys):
    A = []
    D = []
    C = []
    for i in range(1,k+2):
        C.append(1)
        for j in range(1,k+1):
            C.append(i**j)
        A.append(C)
        D.append(keys[i-1])
        C = []
    a = np.array(A)
    d = np.array(D)
    x = np.linalg.solve(a,d)

    return int(x[0])

if __name__ == '__main__':
    ''' 
    Call split_secret() to generate keys
    Call get_secret() to recover your original secret
    Disclaimer: get_secret() just takes the first k keys and assumes
    they are in order, this can be easily implemented for any keys 
    in any order, but this code is simply to highlight the simplicity 
    of the (k, n) threshold scheme
    '''
    keys = split_secret('12345678910',3,5)
    recovered_secret = get_secret(3,keys)
    print(recovered_secret)    


    '''  
    Thanks to Vincent Chiodo and Isroel Kogan for review of the code
    Thanks to Kenso Trabing for the inspiration, and ByteAcademy in NY 
    for teaching me Python
    ''' 


















