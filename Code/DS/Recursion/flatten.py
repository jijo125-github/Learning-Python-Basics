def flatten(arr):
    """ recursive function which accepts an array of arrays and returns a new array with all values flattened """
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr

arrr = [1, [2, [3,4], [[5]]]]
print(flatten(arrr)) 
