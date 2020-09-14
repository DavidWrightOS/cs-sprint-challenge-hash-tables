def has_negatives(a):
    nums_dict = {}
    result = []

    for num in a:
        abs_num = abs(num)
        if abs_num in nums_dict:
            value = nums_dict[abs_num]
            if value == 0:
                continue
            elif value + num == 0:
                result.append(abs_num)
                nums_dict[abs_num] = 0
        else:
            nums_dict[abs_num] = num  

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
