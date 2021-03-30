def bubble_sort(num_list):
    """ Sort with bubble sort """
    length = len(num_list)
    for i in range(length-1, 0, -1):
        for index in range(i):
            if num_list[index] > num_list[index + 1]:
                num_list[index], num_list[index+1] = num_list[index+1], num_list[index]

        print("Sorted till index: ", index)
        print(num_list)

    print("Sorted list is: ", num_list)


number_list = [11, 4, 28, 15, 32, 9, 77]
bubble_sort(number_list)
