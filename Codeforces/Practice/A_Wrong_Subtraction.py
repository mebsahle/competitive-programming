n, k = map(int, input().split())
while k:
    if str(n)[-1] == '0':
        n//=10
    else:
        n-=1

    k-=1

print(n)