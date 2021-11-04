
# Function that determinate the amount of occurences of given items 
## it iterates through the data structures and if it get a match on the latter (given items) it will increment and finnally return it
def get_occurence(struct, i):
    ocr = 0
    for k in struct:
        if k == i:
            ocr = ocr + 1
    return ocr

# Printing the Final Result

print(get_occurence([1, 2, 1, 1, 1], 1))