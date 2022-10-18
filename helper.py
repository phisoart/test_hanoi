import numpy as np

def hanoi_print(_src, _aux, _des):
    _n = len(_src)
    print('=========================')
    for i in range(_n):
        print('|\t' + str(int(_src[i])) + '\t\t' + str(int(_aux[i])) + '\t\t' + str(int(_des[i])) + '\t|')
    print('|\tsrc\t\taux\t\tdes\t|')
    print('=========================')

def hanoi_init(_height):
    return np.arange(1, _height+1), np.zeros(_height), np.zeros(_height)