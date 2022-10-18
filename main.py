import numpy as np

def test():
    return True

def hanoi_print(_src, _aux, _des):
    _n = len(_src)
    print('=========================')
    for i in range(_n):
        print('|\t' + str(_src[i]) + '\t\t' + str(int(_aux[i])) + '\t\t' + str(int(_des[i])) + '\t|')
    print('|\tsrc\t\taux\t\tdes\t|')
    print('=========================')

def hanoi_init(_height):
    return np.arange(1, _height+1), np.zeros(_height), np.zeros(_height)

def hanoi(_height, _algorithm):
    source, auxiliary, destination = hanoi_init(_height)
    hanoi_print(source, auxiliary, destination)
    # print(input)
    # output, comp_n = algorithm (input)
    # print(output)
    # return comp_n

if __name__ == '__main__':
    height = 10

    # if ~test(Algorithm ###):
    #     print ('test fail')

    comp_n = hanoi(height, "")

    # print(height, comp_n)
