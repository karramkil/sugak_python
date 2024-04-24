def insert_value_in_ordered_list(lst, value):
    index = 0
    while index < len(lst) and lst[index] < value:
        index += 1
    lst.insert(index, value)
    return lst
