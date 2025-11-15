
t = int(input())

for _ in range(t):
    n = int(input())
    arr =list(map(int,input().split()))
    arr[arr.index(min(arr))] = arr[arr.index(min(arr))] + 1
    
    products = 1
    for i in arr:
        products = products * i  
    
    print(products)
