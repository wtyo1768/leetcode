

def combine(a1, a2):
    arr = []
    i, j = 0, 0
    l1, l2 = len(a1), len(a2)

    while i<l1 or j<l2:
        if i<l1 and j<l2:
            if a1[i]<a2[j]:
                arr.append(a1[i])
                i+=1
            else:
                arr.append(a2[j])
                j+=1
        elif i<l1:
            arr.append(a1[i])
            i+=1
        else:
            arr.append(a2[j])
            j+=1
    return arr


def mergeSort(arr):
    if len(arr)<=1 : return arr

    m = len(arr) // 2

    l = mergeSort(arr[:m])
    r = mergeSort(arr[m:])
    return combine(l, r)




def mergeSort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr) // 2

    l, r = arr[:mid], arr[mid:]
    
    l = mergeSort(l)
    r = mergeSort(r)

    new_arr = []
    i, j = 0, 0 
    while(i<len(l) or j<len(r)):
        if i<len(l) and j<len(r) :
            if l[i]<r[j]:
                new_arr.append(l[i])
                i+=1
            else:
                new_arr.append(r[j])
                j+=1
        elif i<len(l):
            new_arr.append(l[i])
            i+=1
        else:
            new_arr.append(r[j])
            j+=1
    return new_arr

arr = [10, 80, 30, 90, 40, 50, 70]
arr =  mergeSort(arr)
print(arr)

arr = [12, 11, 13, 5, 6, 7]
arr = mergeSort(arr)
print(arr)

arr = [9,8,7,6,5,4,3,2,1]
arr = mergeSort(arr)
print(arr)