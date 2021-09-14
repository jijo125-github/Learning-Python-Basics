def merge_sort(num_list):
    if len(num_list) <= 1:
        return

    mid = len(num_list) // 2
    left_half = num_list[:mid]
    right_half = num_list[mid:]

    merge_sort(left_half)
    print(left_half)

    merge_sort(right_half)
    print(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            num_list[k] = left_half[i]
            i = i + 1
        else:
            num_list[k] = right_half[j]
            j = j + 1
        k = k + 1

    while i < len(left_half):
        num_list[k] = left_half[i]
        i = i + 1
        k = k + 1

    while j < len(right_half):
        num_list[k] = right_half[j]
        j = j + 1
        k = k + 1

    print("Sorted list: ", num_list)


org_list = [66, 33, 22, 44, 88, 11, 9, 3, 123]
merge_sort(org_list)
