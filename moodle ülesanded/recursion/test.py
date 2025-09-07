import recursion

if __name__ == '__main__':
    array_list = [1,2,[3, [3,[5,[6,[7,8,10]]]]],[7,8], [5, 6]]
    value_list = [[3, 4], [5, 6]]
    # nested_list1 = value_list[0]
    # nested_list1_sum = value_list[0][0] + value_list[0][1]
    #
    # nested_list2 = value_list[1]
    # nested_list2_sum = value_list[1][0] + value_list[1][1]

    # print(nested_list1 + nested_list2)
    # print("SUM1: ",nested_list1_sum)
    # print("SUM2: ", nested_list2_sum)
    check = 8
    if check == 0:
        recursion.loop_reverse('backwards')
    if check == 1:
        print(recursion.recursive_reverse('aaa'))
    if check == 2:
        print(recursion.loop_sum(5))
    if check == 3:
        print(recursion.recursive_sum(5))
    if check == 4:
        print(recursion.sum_digits_recursive(123436))
    if check == 5:
        print(recursion.pair_star_recursive('hello'))
    if check == 6:
        print(recursion.nested_list(value_list))
    if check == 7:
        print(recursion.nested_for_loop(value_list))
    if check == 8:
        print(recursion.array_list(array_list))
        print(recursion.array_list_loop(array_list))