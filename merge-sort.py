#! /usr/bin/python3

a_list = [1,3,8,4,11,5,10]
b_list = [-1, 50, 6, 51, 0]

def sort_list(inlist):
    list_sorted=[]
    for i in range(len(inlist)):
         temp = min(inlist)
         list_sorted.append(temp)
         inlist.remove(temp)
    return list_sorted

def merged(a_list, b_list):
    merge = a_sorted = b_sorted = []

    a_sorted = sort_list(a_list)
    b_sorted = sort_list(b_list)
    merge = a_sorted+b_sorted
    merge_sorted = sort_list(merge)

    return merge_sorted

mer = merged(a_list, b_list)
print("The combined sorted list is:", mer)

