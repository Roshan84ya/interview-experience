for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    count = 1
    for j in range(1,n):
        if (a[j-1] <= a[j]):
            count += 1
        else:
            ans += ((count)*(count + 1))//2
            count = 1
    ans += ((count)*(count + 1))//2
    print(ans)