

def insert_sorted(lst, k):
    for i in range(len(lst)):
        if lst[i] > k:
            lst.insert(i, k)
            return lst
    lst.append(k)
    return lst