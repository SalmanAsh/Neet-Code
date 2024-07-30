def getMinimumUniqueSum(arr):
    arr.sort()
    unique_sum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            arr[i] = arr[i - 1] + 1
        unique_sum += arr[i]
    return unique_sum

# Example usage
arr = [3, 1, 2, 2]
print(getMinimumUniqueSum(arr))  # Output should be 10