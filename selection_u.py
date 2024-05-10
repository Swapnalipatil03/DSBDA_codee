def selection_sort(arr):
    # Loop through each element in the array
    for i in range(len(arr)):
        # Assume the current index is the index of the minimum value
        min_idx = i
        
        # Iterate over the remaining elements to find the index of the minimum value
        for j in range(i+1, len(arr)):
            # Compare the current element with the element at min_idx
            if (arr[j]) < arr[min_idx]:
                # If the current element is smaller, update min_idx to the current index
                min_idx = j
        
        # Swap the value at the current index with the value at min_idx
        # This moves the minimum value to its correct position in the sorted portion of the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Return the sorted array
    return arr

# Take user input to define the unsorted list
input_str = input("Enter the elements of the list separated by spaces: ")
my_list = list(map(int, input_str.split()))

# Call the selection_sort function to sort the list
sorted_list = selection_sort(my_list)

# Print the sorted list
print("Sorted list:", sorted_list)
