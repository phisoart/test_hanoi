import helper

def hanoi_test(_algorithm):
    source, auxiliary, destination = helper.hanoi_init(10)
    _src, _aux, _des, _comp_n = _algorithm(len(source), source, auxiliary, destination, 0)

    # 길이가 모두 동일한지 확인.
    if not (len(_src)==len(_aux)==len(_des)):
        print("길이가 다름.")
        return False

    # 정답 맞는지 확인.
    for i in range(len(_src)):
        if _src[i] != 0:
            print("src가 틀림.")
            return False
        if _aux[i] != 0:
            print("aux가 틀림.")
            return False
        if _des[i] != i+1:
            print("des가 틀림.")
            return False
    return True
