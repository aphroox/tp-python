
# factorial function 
def factorial(a):
    # End of recursion criteria (this will stop the recursion)
    if a == 1: return a
    # Determinate the factorial by recursion
    return a * factorial(a - 1)

# Main function <== 
def determinate(c):
    # Declaration of the accumaltor variable (final result) 
    result = 0
    # Declaration of the main loop that reduce to last 
    for i in range(1, c + 1):
        result = (factorial(i)/i) + result
    # Final result 
    return result

# affichage de la resultat final
print(determinate(int(input("hello put my things here \n"))))
