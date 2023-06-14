#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map
def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))
