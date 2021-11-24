#!/usr/bin/python3
def subs(list_number):
    sub = 0
    max_list = max(list_number)

    for num in list_number:
        if max_list > num:
            sub += num

    return (max_list - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_number.keys())

    numbers = 0
    last_roman_num = 0
    list_number = [0]

    for string in roman_string:
        for roman_num in list_keys:
            if roman_num == string:
                if roman_number.get(string) <= last_roman_num:
                    numbers += subs(list_number)
                    list_number = [roman_number.get(string)]
                else:
                    list_number.append(roman_number.get(string))

                last_roman_num = roman_number.get(string)

    numbers += subs(list_number)

    return (numbers)
