def selection_sort(num_list):
    """ doing selection sort for the list O(N2)"""
    length = len(num_list)

    for i in range(length):
        min_value_index = i
        for j in range(i+1, length):
            if num_list[min_value_index] > num_list[j]:
                min_value_index = j

        num_list[i], num_list[min_value_index] = num_list[min_value_index], num_list[i]
        print("Sorted till index: ", i)
        print(num_list)
        print("")

    print("Sorted List is: ", num_list)


selection_sort([2, 1, 5, 3])
