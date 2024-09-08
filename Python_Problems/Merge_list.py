def merge_list(list1, list2):

    list1.extend(list2)

    return sorted(list1)

list1 = [1,2,4]
list2 = [1,3,4]

print(merge_list(list1, list2))