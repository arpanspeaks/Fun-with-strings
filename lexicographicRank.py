'''
https://practice.geeksforgeeks.org/problems/rank-the-permutations/0
'''

# TC : 0(n)

mod = 1000003
maxx = 257

def fact(n):
    return n if (n < 2) else (n * fact(n-1))
    
def modifyCountArr(countArr, start):
    for i in range(start, maxx):
        countArr[i] -= 1
    return countArr

def getRank(s):
    mul = fact(len(s))
    countArr = [0] * maxx
    rank = 1
    
    for char in s:
        if countArr[ord(char)]:
            return 0
        countArr[ord(char)] = 1
    
    for i in range(1, maxx):
        countArr[i] += countArr[i-1]
    
    for i in range(len(s)):
        mul //= (len(s) - i)
        rank = (rank + (countArr[ord(s[i]) - 1] * mul) % mod) % mod
        countArr = modifyCountArr(countArr, ord(s[i]))
    
    return rank

def main():
    t = int(input())
    while t:
        s = str(input())
        print(getRank(s))
        t -= 1
        
if __name__ == '__main__':
    main()
