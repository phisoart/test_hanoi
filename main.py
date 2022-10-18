import helper
import algorithm

def test():
    return True

def hanoi(_height, _algorithm):
    source, auxiliary, destination = helper.hanoi_init(_height)
    comp_n = 0

    print("start!")
    helper.hanoi_print(source, auxiliary, destination)
    out_source, out_auxiliary, out_destination, out_comp_n = algorithm.algo1(len(source), source, auxiliary, destination, comp_n)

    print("finish!")
    helper.hanoi_print(out_source, out_auxiliary, out_destination)
    return out_comp_n

if __name__ == '__main__':
    height = 4

    # if ~test(Algorithm ###):
    #     print ('test fail')

    comp_n = hanoi(height, "")
    print('height: ' + str(height) + '\ntot move: ' + str(comp_n))
