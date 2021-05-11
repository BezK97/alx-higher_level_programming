#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_unique = my_list[0]
    n = 0
    for i in range(1, len(my_list)):
        for j in range(i):
            if my_list[i] == my_list[j]:
                n = 0
                break
            else:
                n = my_list[i]
        sum_unique += n
    return (sum_unique)
