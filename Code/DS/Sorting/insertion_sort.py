def insertion_sort(num_list):
    """ Implementing insertion sort """
    length = len(num_list)
    for i in range(length-1):
        for j in range(i+1, 0, -1):
            if num_list[j-1] > num_list[j]:
                num_list[j-1], num_list[j] = num_list[j], num_list[j-1]

        print("Sorted till index", i)
        print(num_list)


number_list = [1, 5, 2, 4, 88, 21, 11, 22, 3, 99, 25, 44, 22]
insertion_sort(number_list)
