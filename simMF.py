#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:54:40 2020

@author: smoke
"""
import sys
import numpy as np
from sklearn.model_selection import train_test_split


def matrix_factorization(R, P, Q, K, steps, lr, lambda1,simU,simI, alpha, beta):
    for step in range(steps):
        print(step)
        error = 0
        for i in range(len(R)):
            print("i = ",i)
            eij = R[i][2] - np.dot(P[int(R[i][0]),:],Q[:,int(R[i][1])])
            error += eij
            for k in range(K):
                simregU = 0
                for t in range(len(simU[int(R[i][0])])):
                    simregU += simU[int(R[i][0])][t][1] * ( P[int(R[i][0])][k] - P[int(simU[int(R[i][0])][t][0])][k])
                
                simregI = 0
                for t in range(len(simI[int(R[i][1])])):
                    simregI += simI[int(R[i][1])][t][1] * ( Q[k][int(R[i][1])] - Q[k][int(simI[int(R[i][1])][t][0])])
                    
                P[int(R[i][0])][k] = P[int(R[i][0])][k] + lr * (2 * eij * Q[k][int(R[i][1])] - lambda1 * P[int(R[i][0])][k] - alpha * simregU)
                Q[k][int(R[i][1])] = Q[k][int(R[i][1])] + lr * (2 * eij * P[int(R[i][0])][k] - lambda1 * Q[k][int(R[i][1])] - beta * simregI) 
        print("error ", error)
    return P, Q.T

    

f_in = open("/home/smoke/Documents/ML/project/Datasets/HIN_dataset/Yelp/user_movie.dat","r");
f_in0 = f_in.readlines()[1:];
a = list();
for i in f_in0:
    a.append(list(map(float,i.split())));
f_in.close();
print(len(a))

a.sort(key = lambda x: x[0])
a = np.array(a)
row = a[len(a)-1][0];
a = a.T
col = max(a[1]);

a[0] = list(map(lambda x : int(x-1), a[0]))
a[1] = list(map(lambda x : int(x-1), a[1]))

a = a.T
steps = 20;
lr = 0.002
lambda1 = 0.02
alpha = 0.2;
beta = 0.2;
dim = int(20);

    
print(row,col)
row = int(row)
col = int(col)
U = np.random.rand(row, dim);
V = np.random.rand(dim, col);



in_matrix = [[0.0]*col for i in range(row)];
X_train, X_test = train_test_split(a, test_size = .1);


# took 5% of total users for similarity (top 5% similarity measures for each user and item) 
smallkU = int(0.05*row)
smallkB = int(0.05*col)

#simUList.txt contains 3D data that is stored sequentially
# for each user i, their is a (5% of users)x2 matrix, where first element of each row is the user j 
# and second element is similarity measure between i and j 

finalU = np.loadtxt(r"/home/smoke/Documents/ML/project/Datasets/lists/simUList.txt")
finalU = finalU.reshape((row,smallkU,2))

#simMList.txt contains 3D data that is stored sequentially
# for each item(movie) i, their is a (5% of items)x2 matrix, where first element of each row is the item j 
# and second element is similarity measure between i and j 

finalB = np.loadtxt(r"/home/smoke/Documents/ML/project/Datasets/lists/simMList.txt")
finalB = finalB.reshape((col,smallkB,2))

nU, nV = matrix_factorization(X_train,U,V,dim,steps,lr, lambda1,finalU,finalB, alpha, beta);

print("factorization done!!!");

e = 0;
for i in range(len(X_test)):
    temp = np.dot(nU[int(X_test[i][0])], nV[int(X_test[i][1])]);
    e += pow(temp - X_test[i][2],2);
e /= len(X_test);
print('error ',e**0.5);
