import math

def is_prime(n):
    if n <= 1:
        return False

    # if a number is not divisible by any divisor 
    # from 2 up to the square root of the number,
    # it's a prime number
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def display_primes_starting_with_5():
    for number in range(500, 600):
        if is_prime(number):
            print(number)

# Run the function
display_primes_starting_with_5()
