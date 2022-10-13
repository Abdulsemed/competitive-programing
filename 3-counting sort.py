def countingSort(arr):
    # Write your code here
    
    max_value = max(arr)+1
    if max_value < 100:
        max_value += 1
    count_arr = [0]*max_value
    for elt in arr:
        count_arr[elt] += 1 
    return count_arr
