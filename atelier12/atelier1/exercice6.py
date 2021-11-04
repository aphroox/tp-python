
# Function that Sort by insertion 
### That's by mutating each value in the array according to if its greater than its precedor / next value
def sort_by_insertion(data):
    i =  0
    while( i < len(data) - 1):
        if data[i] > data[i + 1]:
            j = data[i + 1]
            data[i + 1] = data[i]
            data[i] = j
        i = i + 1
    return data

# Function that Sort by Bull
## I the most efficient
### That's by iterating the whole list and getting the minimum each time and append to a new list
def sort_by_bull(data, a):
    if data == []:
        return a
    num1 = min(data)
    a.append(num1)
    data.remove(num1)
    return sort_by_bull(data, list(a))


# Function that Sort by Selection
## Slowest
### That's by choosing a element and comparing it to the rest of the list and mutating if we found greater than the latter 
def sort_by_selection(data):
    n = len(data)
    for i in range(0, n - 2):
        min = i
        for j in range(i + 1, n - 1):
            if data[j] < data[min]:
                min = j
        if min != i:
            temp = data[min]
            data[min] = data[i]
            data[i] = temp
    return data


# affichage Finale
print(sort_by_insertion([7, 45, 8, 2, 1]))
print(sort_by_selection([0, 3, 8, 2, 2]))
print(sort_by_bull([10, 9, 6, 2, 5], []))