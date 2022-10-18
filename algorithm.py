def algo1(_count, src, aux, des, comp_n):
    if _count == 1:
        ##############################
        # move plate
        for iter_src, i_src in enumerate(src):
            if int(i_src) != 0:
                for iter_des, i_des in enumerate(des):
                    if int(i_des) != 0:
                        des[iter_des - 1] = i_src
                        src[iter_src] = 0
                        break
                    if iter_des == len(des) - 1:
                        des[iter_des] = i_src
                        src[iter_src] = 0
                        break
                break
        comp_n = comp_n + 1
        ##############################

        return src, aux, des, comp_n
    else:
        src, des, aux, comp_n = algo1(_count - 1, src, des, aux, comp_n)
        src, aux, des, comp_n = algo1(1, src, aux, des, comp_n)
        aux, src, des, comp_n = algo1(_count - 1, aux, src, des, comp_n)
        return src, aux, des, comp_n
