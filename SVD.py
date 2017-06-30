#! python 
# @Time    : 17-6-30
# @Author  : kay
# @File    : SVD.py
# @E-mail  : 861186267@qq.com
# @Function: this is the demo of how to use SVD method to reduce dimension
#            for extract important features

import string
import types
from numpy import *
from numpy.linalg import svd

def svd_process():
    # the initial matrix targeted to dealt
    # MxN: 3x5
    init_matrix = array([
        [1., 0., 0., 1., 1.],
        [1., 0., 1., 0., 1.],
        [0., 1., 0., 0., 1.],
    ])

    print(init_matrix)
    T, S, D = svd(init_matrix)

    for x in T:
        print('T:', around(x, decimals=2))
    print('----------------------------------------------------')

    for x in S:
        print('S:', around(x, decimals=2))
    print('----------------------------------------------------')

    for x in D:
        print('D:', around(x, decimals=2))
    print('----------------------------------------------------')

    key_dim = 2 # the dimension wish to left
    S_ = zeros(shape=(key_dim, key_dim))
    S_[:key_dim, :key_dim] = diag(S[:key_dim])
    T_ = delete(T, s_[key_dim:], axis=1)
    D_ = delete(D, s_[key_dim:], axis=0)

    for x in T_:
        print('T_:', around(x, decimals=2))
    print('----------------------------------------------------')

    for x in S_:
        print('S_:', around(x, decimals=2))
    print('----------------------------------------------------')

    for x in D_:
        print('D_:', around(x, decimals=2))
    print('----------------------------------------------------')

    out_matrix=dot(T_, dot(S_, D_))

    for x in out_matrix:
        print('out_matrix:', around(x, decimals=2))

if __name__ == '__main__':
    svd_process()
