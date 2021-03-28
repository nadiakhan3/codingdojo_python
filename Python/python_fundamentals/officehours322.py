def length_and_value(x,y):
    arr=[]
    for i in range (x):
        if len(arr)<x:
            arr.append(y)
    print(arr)

length_and_value(5,8)


def officehours(arr):
    newarr=[]
    for i in arr:
        if i > arr[1]:
            newarr.append(i)
    print(newarr)
    print(len(newarr))

officehours([1,3,5,6,7,8])


def cool(list):
    return len(list)

cool([1,5,6,8,3,5])