# Function convert Number to inversed Binary 
def binary(num):
    # Allocation of the Final Result
    result = ""
    # End of Recursion Criteria (end of Recursion)
    if num >= 1:
        # Concatenates 0s and 1s 
        result = result + str(num % 2)
        # Start of Recursion 
        # num // 2 designate Clean Division without without remainder
        return result + binary(num // 2)
    # End of Function after the End of recursion fails
    return result

# Function that reverse a String to get a valide binary representation
def reverse(string):
    return string[::-1]

# Main Function
def main(num):
    return (reverse(binary(num)))

# Printing the result 
print(main(int(input("enter the number here pls \n"))))