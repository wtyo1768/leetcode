def heapify(arr, n, i):
    l, r = 2*i+1, 2*i+2
    largest = i
    print(arr)
    if l<n and arr[l]>arr[largest]:
        largest = l 
    if r<n and arr[r]>arr[largest]:
        largest = r
    
    if not largest==i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

 
# The main function to sort an array of given size
 
 
def heapSort(arr):
    n = len(arr)
    
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
 
# Driver code
# arr = [12, 11, 13, 5, 6, 7]
arr = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]

heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
# This code is contributed by Mohit Kumra


def set_list(list):
    list = ["A", "B", "C"]
    return list
  
def add(list):
    list.append("D")
    return list
  
my_list = ["E"]
  
print(set_list(my_list))
  
print(my_list)

print(add(my_list))

print(my_list)