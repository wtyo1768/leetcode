



def outter():
    a = 1
    arr = []

    def inner():
        nonlocal a
        a+=1
        arr.append([3])

        print(a, arr)

    inner()
    print(a, arr)

outter()

a = (3, 5)
a += (6,)
print(a)