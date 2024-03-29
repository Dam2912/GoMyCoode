#sub seq
def max_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [1, 1, -3, 4, -5, 2, 7, -1]
max_sum = max_subarray_sum(arr)
print(max_sum)

