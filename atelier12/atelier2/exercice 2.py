def divide_conquere(data):
    i = 0
    export = []
    for i in range(0, 9, 3):
        export.append(data[i:i + 3])
    return export


print(divide_conquere([5, 2, 3, 7, 5, 6, 72, 4, 9]))