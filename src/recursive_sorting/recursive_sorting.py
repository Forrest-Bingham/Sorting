# TO-DO: complete the helpe function below to merge 2 sorted arrays

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arrA = [4, 2, 8, 6]
arrB = [3,5, 0, 1, 9]
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    x = 0
    # TO-DO
    while(len(arrA) >= 1 and len(arrB) >= 1):
        #print(arrA[i], arrB[j])
        if arrA[0] <= arrB[0]:
            merged_arr[x] = arrA[0]
            #print(arrA[0], "-- Value added to merged array")
            del arrA[0]
            x += 1
            #print(merged_arr, "Merged Array")
        else:
            merged_arr[x] = arrB[0]
            #print(arrB[0], "-- Value added to merged array")
            del arrB[0]
            x += 1
            #print(merged_arr, "Merged Array")
    #print(merged_arr)

    #print(arrA, "arrA")
    #print(arrB, "arrB")
    while len(arrA) >= 1:
        merged_arr[x] = arrA[0]
        del arrA[0]
        x += 1
        #print(merged_arr)
    while len(arrB) >= 1:
        merged_arr[x] = arrB[0]
        del arrB[0]
        x += 1
        #print(merged_arr)
    
    return merged_arr

# merge(arrA, arrB)

# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:    # Base case
        return arr
    half = len(arr)//2
    arrA = arr[:half]
    arrB = arr[half:]
    # print(arr)
    # print(arrA)
    # print(arrB)

    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)

    print(arr)
    return merge(arrA, arrB)

merge_sort(arrA)
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
