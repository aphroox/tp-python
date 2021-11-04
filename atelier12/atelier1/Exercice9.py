def get_coordinate(matrix, elem):
    for i in matrix:
        for j in i:
            if j == elem:
                return [i, j]
    return None

print(get_coordinate(list(input("put a number")), 1))
