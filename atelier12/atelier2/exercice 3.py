def occurence(list1):
    a = {}
    for i in list1:
        if str(i) in a:
            a[str(i)] = a.get(str(i)) + 1
        else:
            a[str(i)] = 1
    return a

print(occurence(2, 4, 3, 7, 5,1,]))