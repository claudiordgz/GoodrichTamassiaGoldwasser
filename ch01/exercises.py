# coding=utf-8
__author__ = 'Claudio'

if __name__ == "__main__":
    l = [2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]


    print(range_from_eigth())
    print(list_comprehension_example())
    print(custom_choice(l))
    print(custom_choice(l))
    print(custom_choice(l))
    print(custom_choice(l))
    print(custom_choice(l))
    print(custom_reverse(l))
    print(get_odd_numbers(l))
    print(check_if_unique(l))
    print(check_if_unique(l[:7]))
    l2 = [MutableNum(x) for x in l]
    print(scale(l2, 5))
    print(demonstration_list_comprehension())
    print(demonstration_list_comprehension_abc())
    print(custome_shuffle(l))
    s = list()
    read_sdin(s)