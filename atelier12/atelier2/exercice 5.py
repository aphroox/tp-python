def get_by(list1, dict1):
    keys = list(dict1.keys())
    result = []
    for i in keys:
        for j in list1:
            if dict1[str(i)] == j: result.append(j)
    return result

print(get_by([48, 23, 69, 37, 76, 83, 89, 36], {'najib':47, 'salma':69, 'Mohammed':76, 'Abir':89}))