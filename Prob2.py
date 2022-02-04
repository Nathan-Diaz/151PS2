########################################
# Name: Nathan G. Diaz 
# Collaborators: N/A
# Estimated time spent (hr): 4
########################################

def approximate_pi(n_terms):
    "Preparation Code"
    NthValue = 2*n_terms - 1 # provides the value of the n-th odd number
    NthValue += 1            # alters NthValue so that NthValue will be inluded in range later on
    pi = 0                   # defines pi as a number
    lst = list(range(1, NthValue, 4)) # creates a list that contains every other odd number
    print(lst, "are the denominators to be added in Leibniz's series")
    # numbers not in the list are the numbers in the numerator to be substrated in Leibniz's series

    "Functioning Code"
    for i in range(1, (NthValue), 2):
        if i in lst:
            pi += 1/i
        else: 
            pi -= 1/i
    pi = 4*pi
    
    return (pi)

if __name__ == '__main__':
    # You can alter the below value to test your function with a variety
    # of numeric inputs!
    test_num_terms = 5
    print("Pi is approximately ", approximate_pi(test_num_terms), " using ", test_num_terms, " terms.")

##### Logic Behind Code #####
""" Approximates the value of pi using Leibniz's series. 
    Step 1: Determine the numerical value of n-th term known as NthValue. 
    Step 2: Create a list, known as lst, which contains every other odd number starting at 1 till NthValue. 
    Step 3: Compare every odd number from 1 till NthValue to list and alter pi accordingly.
            Since every other odd number starting at 1 is added and 
            every other odd number starting at 3 is substrated,
            the comparision of every odd number within the list 
            determines wheather of not the faction associated with the odd number 
            will be added or substracted. 
    Step 4: Mltiple pi by 4. """
