#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    element = my_list[idx]
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list.remove(element)
    return (my_list)
