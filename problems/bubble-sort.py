n = int(input("Enter number of elements in array: "))
arr = []
for i in range(n):
    arr.append(int(input()))
def bubble_sort(arr):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(arr))