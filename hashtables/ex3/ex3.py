def intersection(arrays):
    list_count = len(arrays)
    elem_count = {}
    for array in arrays:
        for elem in array:
            elem_count[elem] = elem_count[elem] + 1 if elem in elem_count else 1
    return [elem for elem in elem_count.keys() if elem_count[elem] == list_count]    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
