def find_second_smallest(my_list):
    sorted_list = sorted(my_list)
    length = len(sorted_list)
    if length < 2:
        return None
    else:
        return sorted_list[1]

print(find_second_smallest([5, 8, 3, 2, 6]))
