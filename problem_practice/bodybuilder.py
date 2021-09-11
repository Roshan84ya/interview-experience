for i in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    m = 0
    current = 0
    for i in range(len(b)):
        current = current + b[i]
        m = max(current, m)
        if (i < (len(b)-1)):
            current = max(0,current - (a[i+1] - a[i])*k)
    print(m)
