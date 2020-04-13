# TO-DO: Complete the selection_sort() function below 
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        
        cur_index = i
        smallest_index = cur_index

        print("smallest index --", smallest_index, "current index", cur_index)
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        #First Array:   arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        # Should return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(i, "-- index, value --", arr[i])

        #"This is finding the smallest value in the array")
        for x in range(i+1, len(arr)):  #i+1 since i is going to be the sorted part of the array
            print(arr[x], "-- x, smallest_index --", arr[smallest_index])
            if arr[x] < arr[smallest_index]:
                smallest_index = x
        
        # TO-DO: swap
        #This puts the lowest value of the above array into the sorted array.
        print("before --", arr[i])
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        print("After --", arr[i])

    return arr

# selection_sort(arr1)
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    bubble = arr
    print("bubble", arr)
    for x in range(len(bubble)):
        print(x, "--X")
        print(bubble)
        for y in range(0,len(bubble)-x-1):
            print("y--", y, "value --", arr[y])
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]

    print(bubble)
    return arr

bubble_sort(arr1)
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr