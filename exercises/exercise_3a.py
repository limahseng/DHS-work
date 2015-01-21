__author__ = 'dhs'

def is_prime(number):
    for integer in range(2,10): # gisc: should not restrict to division till 10 only
        if integer >= number:
            #if the number is within 2 to 10, without this condition, the function might give a wrong answer!
            break
        if number % integer == 0: # gisc: some divisions are unnecessary
            return False
    return True

tested = int(input("Input an integer from 1 to 100!")) # gisc: too restrictive

if 0 < tested <= 100:

    if is_prime(tested) == True:
        print(tested, "is a prime number!")
    else:
        print(tested, "is not a prime number!")

else:
    print("That is not an integer from 1 to 100!")
