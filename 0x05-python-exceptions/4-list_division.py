def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("Division by 0")
            result = 0
        except TypeError:
            print("Wrong type")
            result = 0
        except IndexError:
            print("Out of range")
            result = 0
        finally:
            new_list.append(result)

    return new_list
