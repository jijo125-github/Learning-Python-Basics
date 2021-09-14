def array_advance(arr):
    furthest_reached = 0
    last_index = len(arr) - 1
    i = 0
    while i <= furthest_reached < last_index:
        furthest_reached = max(furthest_reached,arr[i] + i)
        i += 1
    return furthest_reached >= last_index


arr1 = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(arr1))

arr2 = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(arr2))
