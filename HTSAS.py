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
    #Create two empty lists and a dictionary
    D = {}
    A = []
    B = []
    
    #Set A0 to be the secret, as defined a0 = D
    A.append(int(secret))

    #Fill the rest of the list A, from A1 to An, with 
    #random numbers, as defined in paper "we pick a random
    # k-1 polynomial"
    for j in range(1,n):
        A.append(random.randrange(1,100))

    #Evaluate each polynomial, q(i)
    for i in range(1,n+1):
        #First item is A0
        B.append(A[0])
        #Every other item is evaluated by substituting x 
        for j in range(1,k):
            B.append(A[j]*i**j)
        #Sum all the polynomial terms, save sum as Di
        #these are your keys
        D[i] = sum(B)

        B = []  #reset B in order to use again empty 

    return D

def get_secret(k,keys):
    ''' 
    k is the number of keys you are supplying
    ''' 

    #Create 3 empty lists
    A = []
    D = []
    C = []
    
    #Re-create the polynomials to solve
    # for the coefficients 
    for i in range(1,k+2):
        C.append(1)
        for j in range(1,k+1):
            C.append(i**j)
        A.append(C)
        D.append(keys[i-1])
        C = []

    #Solve Ax = D
    # x are our coeeficients(a0 to an)
    a = np.array(A)
    d = np.array(D)
    x = np.linalg.solve(a,d)

    #The original Secret is a0
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


















