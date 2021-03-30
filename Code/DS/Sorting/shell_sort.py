def shell_sort(num_list):
    """  Implement shell sort"""
    length = len(num_list)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            temp = num_list[i]
            j = i
            while j >= gap and num_list[j-gap] > temp:
                num_list[j] = num_list[j - gap]
                j -= gap
            num_list[j] = temp
            print("Gap: ", gap)
            print(num_list)
        gap = gap // 2


arr = [1, 3, 2, 4, 7, 22, 99, 33]
shell_sort(arr)
