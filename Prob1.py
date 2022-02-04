########################################
# Name:
# Collaborators:
# Estimated time spent (hr):
########################################

def digital_root(n):
    """Computes and returns the digital root of a given integer n.

    If you want to define any other function(s) to help you
    out, feel more than free, just make sure this is the main
    function, as this is what will be tested against.

    Inputs:
        n (int): The number to take the digital root of
    Outputs:
        int: The digital root of the provided number
    """

    t = n % 9 
    if (t == 0): # if t is 0, then the digital root is 9
        print(9)
    else: print(t)
    return (t)

if __name__ == '__main__':
    # You can alter the below value to test your function with a variety
    # of numeric inputs!

    test_input = 1729
    print("The digital root of ", test_input, " is ", digital_root(test_input))








if __name__ == '__main__':
    # You can alter the below value to test your function with a variety
    # of numeric inputs!

    test_input = 1729
    print("The digital root of ", test_input, " is ", digital_root(test_input))
