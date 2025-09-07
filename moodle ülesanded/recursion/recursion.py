"""Recursion exercises."""


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    loop_reverse("hey") => "yeh"
    loop_reverse("aaa") => "aaa"
    loop_reverse("") => ""
    loop_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    return s[::-1]


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    recursive_reverse("hey") => "yeh"
    recursive_reverse("aaa") => "aaa"
    recursive_reverse("") => ""
    recursive_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    if len(s) == 1:
        return s
    else:
        return s[-1] + recursive_reverse(s[:-1])


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    loop_sum(0) => 0
    loop_sum(3) => 6
    loop_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    total = 0
    for i in range(n + 1):
        total += i
    return total


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    recursive_sum(0) => 0
    recursive_sum(3) => 6
    recursive_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    if n == 0:
        return n
    else:
        return n + recursive_sum(n - 1)


def sum_digits_recursive(number: int) -> int:
    """
    Return the sum of the digits in number.

    Given a non-negative int n, return the sum of its digits recursively (no loops).

    sum_digits_recursive(123) => 6
    sum_digits_recursive(1) => 1
    sum_digits_recursive(0) => 0
    sum_digits_recursive(999) => 27

    :param number: non-negative number
    :return: sum of digits in the number
    """
    remains = number % 10
    if number < 10 :
        return number
    else:
        return remains + sum_digits_recursive(((number - remains) // 10))


def pair_star_recursive(s: str) -> str:
    """
    Add star between identical adjacent chars.

    Given a string, compute recursively a new string
    where identical chars that are adjacent in the original string
    are separated from each other by a "*".

    :param s: input string
    :return: string with stars between identical chars.
    """
    if len(s) == 1:
        return s
    elif s[0] == s[1]:
        return s[0] + "*" + pair_star_recursive(s[1:])
    else:
        return s[0] + pair_star_recursive(s[1:])


def nested_list(number_list):
    print("List: ", number_list)

    if type(number_list[0]) == type([]):
        return number_list[0][0:]
    elif len(number_list) <= 1:
        return number_list[0]

    print(number_list[0], "+", number_list[1:])
    return number_list[0] + nested_list(number_list[1:])


def array_list(number_list):
    # checks if the list is the length of 1
    if type(number_list[0]) == type([]):
        number_list[0] = array_list(number_list[0])

    if len(number_list) == 1:
        #returns current number
        return number_list[0]
    #takes the first number in the array and sends the rest of the numbers into a recursive loop
    return number_list[0] + array_list(number_list[1:])

def array_list_loop(number_list):
    total = 0
    print(number_list)
    for x in number_list:
        if type(x) == type([]):
            x = array_list_loop(x)
        total += x
    return total

def nested_for_loop(number_list):
    new_array = []
    total = 0
    for i in number_list:
        for x in i:
            new_array.append(x)
            total += x
    print(total)
    return new_array