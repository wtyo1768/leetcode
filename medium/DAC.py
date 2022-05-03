def DAC_Max(a, index, l):
    max = -1
    
    if (index >= l - 2):
        if (a[index] > a[index + 1]):
            return a[index]
        else:
            return a[index + 1]
 
    # Logic to find the Maximum element
    # in the given array.
    max = DAC_Max(a, index + 1, l)
    print(a, a[index], max)
    if (a[index] > max):
        return a[index]
    else:
        return max

if __name__ == '__main__':
   
    # Defining the variables
    min, max = 0, -1
 
    # Initializing the array
    a = [70, 250, 50, 80, 140, 12, 14]
 
    # Recursion - DAC_Max function called
    max = DAC_Max(a, 0, 7)
 
    print("The maximum number in a given array is : ", max)
 
# This code is contributed by 29AjayKumar