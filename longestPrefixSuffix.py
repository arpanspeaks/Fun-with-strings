'''
Longest Prefix Suffix

https://practice.geeksforgeeks.org/problems/longest-prefix-suffix/0

TC: O(n)
'''

def computeLPS(s, lps):
    prevLps = 0
    i = 1
    while i < len(s):
        if s[i] == s[prevLps]:
            prevLps += 1
            lps[i] = prevLps
            i += 1
        else:
            if prevLps == 0:
                lps[i] = 0
                i += 1
            else:
                prevLps = lps[prevLps-1]
    return lps[len(lps)-1]
    
def main():
    t = int(input())
    while t:
        s = str(input())
        lps = [0] * len(s)
        print(computeLPS(s, lps))
        t -= 1
        
if __name__ == '__main__':
    main()
