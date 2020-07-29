# https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring/0

# TC: O(n)

def getLength(s):
    
    lookUp = [-1] * 256
    start, res = 0, 0
    
    for i in range(len(s)):
        start = max(start, lookUp[ord(s[i])] + 1)
        maxx = i - start + 1
        
        res = max(res, maxx)
        lookUp[ord(s[i])] = i
        
    return res
    

def main():
    t = int(input())
    while t:
        s = str(input())
        print(getLength(s))
        t -= 1
        
if __name__ == '__main__':
    main()