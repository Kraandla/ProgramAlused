def factorial_r(x):
    """
    1st step:
    takes 5
    checks if 5 is less than 0
    it is not so it goes to the else statement
    before it can multiply 5 with a number it needs to send another number (in this case x - 1 aka 4)
    to the same function
    2nd step:
    it takes 4 checks if its less than 0
    it goes to the else statement
    3rd step:
    it takes 3 and checks if its less than 0
    it goes to the else statement
    4th step:
    check
    else statement
    5th step:
    check else
    6th step:
    check is true
    returns 0
    7th step:
    the above recursion is 1
    now the calculation in the return statement activates
    it returns 1 * 0 which equals 0
    it does this with the others which makes the total sum of the returned 0
    which means the recursion check cannot be x < 0
    it cannot be x < 1 because it would still be able to return 0
    so the check has to be x == 1
    :param x:
    :return:
    """
    if x == 1:
        return x
    else:
        return x * factorial_r(x - 1)

def zipmap(keys, values):
    return dict

if __name__ == '__main__':
    # print(factorial_r(1))
    zipped = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
    )
    print(zipped)