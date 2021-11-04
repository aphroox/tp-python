s=0
# Function that Determinate the Sommation of number 
def sum(n):
    # End of Recursion Criteria (End of Recursion)
    if n >= 1:
        # Recursion Loop 
        return n + sum( n - 1 )
    # Retrun of the Result
    return n

# Printing the final result
print(sum(int(input("get here the n \n"))))