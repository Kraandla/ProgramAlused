def sum_list(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_list(num_list[1:])

def sum_of_digits(integer):
    int_to_str = str(integer)
    total = 0
    for x in int_to_str:
        print(x)
        total += int(x)
    return total

def sum_of_digits_r(integer):
    next_step = integer // 10
    if integer < 10:
        return integer
    return integer % 10 + sum_of_digits_r(next_step)

def sumDigits(n):
    # Check if 'n' is 0 (base case for summing digits)
    if n == 0:
        # If 'n' is 0, return 0 (no digits to sum)
        return 0
    else:
        # If 'n' is not 0, calculate the sum of the last digit (n % 10) and
        # recursively call the sumDigits function on the remaining digits (n / 10)
        return n % 10 + sumDigits(int(n / 10))

def nested_list_sum(value_list: list):
    # checks if the list is the length of 1
    if type(value_list[0]) == type([]):
        value_list[0] = nested_list_sum(value_list[0])

    if len(value_list) == 1:
        #returns current number
        return value_list[0]
    #takes the first number in the array and sends the rest of the numbers into a recursive loop
    return value_list[0] + nested_list_sum(value_list[1:])

def sum_of_series(n):
    if n <= 0:
        return 0
    return n + sum_of_series(n - 2)
def sum_series(n):
    # Check if 'n' is less than 1 (base case for the series)
    if n < 1:
        # If 'n' is less than 1, return 0 (base case value for the sum)
        return 0
    else:
        # If 'n' is greater than or equal to 1, calculate the sum of 'n' and
        # recursively call the sum_series function with 'n - 2'
        return n + sum_series(n - 2)


def harmonic_series(n):
    if n < 2:
        return n
    return 1 / n + harmonic_series(n - 1)
def harmonic_sum(n):
    # Check if 'n' is less than 2 (base case for the harmonic sum)
    if n < 2:
        # If 'n' is less than 2, return 1 (base case value for the harmonic sum)
        return 1
    else:
        # If 'n' is greater than or equal to 2, calculate the reciprocal of 'n'
        # and add it to the result of recursively calling the harmonic_sum function with 'n - 1'
        return 1 / n + harmonic_sum(n - 1)


def geometric_series(n):
    series = 2 ** n
    print(f"1/{series}")
    if series <= 2:
        return 1/2
    return 1 / series + geometric_series(n - 1)
# Define a function named geometric_sum that calculates the geometric sum up to 'n' terms
def geometric_sum(n):
    # Check if 'n' equals 0, which is the base case for the geometric sum
    if n == 0:  # Corrected base case condition
        # If 'n' equals 0, return 1 as the geometric sum in this case is 1
        return 1
    else:
        # If 'n' is not 0, calculate the term in the geometric series (1 / 2^n) and add it to
        # the result of recursively calling the geometric_sum function with 'n - 1'
        return 1 / (pow(2, n)) + geometric_sum(n - 1)


def recursion_exponentiation(a, b):
    if b == 1:
        return a
    return a * recursion_exponentiation(a, b - 1)


def greatest_divisor(a,b):
    pass


if __name__ == '__main__':
    current_values = []
    nested_array = []
    # print(sum_list([2,3,[5,6],7]))
    # print(nested_list_sum([1, 2, [3, 4], [5, 6]]))
    # print(sum_of_digits_r(1205678930345680))
    # print(sumDigits(1205678930345680))
    # print(sum_of_series(13))
    # print(sum_series(13))
    # print(harmonic_series(13))
    # print(harmonic_sum(13))
    # print(geometric_series(13))
    # print(geometric_sum(13))
    # print(recursion_exponentiation(2, 13))
    print(greatest_divisor(5,5))