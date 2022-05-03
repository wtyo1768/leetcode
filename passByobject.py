
def strFunc(s):

    s+=' Change'

    print(s)


s = 'Original'
print(s)
strFunc(s)
print(s)

def arrFunc(arr):
    arr.append(3)

arr = [1,2,3]
print(arr)
arrFunc(arr)
print(arr)

def turpleFunc(turple):
    turple += (3,)
    print("Inside:", turple)

t = (1,3)
print(t)
turpleFunc(t)
print(t)


def dictFunc(d):
    d['new'] = 213
    print("Inside:", d)


d = {'old':2341}
print(d)
dictFunc(d)
print(d)
