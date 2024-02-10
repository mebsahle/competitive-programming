#User function Template for python3

from collections import Counter
def isSubset( a1, a2, n, m):
    
    d1 = Counter(a1)
    d2 = Counter(a2)
        
    # print(d1)
    # print(d2)
    
    for key, value in d2.items():
        if key not in d1.keys() or d1[key] < value:
                return "No"
    return "Yes"




# Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()
