import helper
import algorithm
import test

def hanoi(_height, _algorithm):
    source, auxiliary, destination = helper.hanoi_init(_height)
    print("start!")
    helper.hanoi_print(source, auxiliary, destination)

    out_source, out_auxiliary, out_destination, out_comp_n = _algorithm(len(source), source, auxiliary, destination, 0)

    print("finish!")
    helper.hanoi_print(out_source, out_auxiliary, out_destination)
    return out_comp_n

if __name__ == '__main__':
    height = 4

    if not test.hanoi_test(algorithm.algo1):
        print ('test fail')
        exit(1)
    else:
        print('테스트 통과!')

    comp_n = hanoi(height, algorithm.algo1)
    print('height: ' + str(height) + '\ntot move: ' + str(comp_n))
