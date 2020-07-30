# https://practice.geeksforgeeks.org/problems/pattern-search-kmp/1/?track=SPC-Strings&batchId=145

'''
Pattern Search KMP 
Given a string S and a pattern P of all lowercase characters. The task is to check if the pattern exists in the string or not.

Input:
The first line of input contains the number of test cases T. For each testcase, the first line of input contains string S and the next line contains pattern P.

Output:
For each testcase, print "Yes" if the pattern is found in the string, and "No" if the pattern is not found in the string.

Your Task:
The task is to complete the function KMPSearch() which returns true or false depending on whether pattern is present in the string or not, and computeLPSArray() which computes the longest prefix suffix for every index.

Expected Time Complexity: O(N+M).
Expected Auxiliary Space: O(M).
Note: N = |S|, M = |P|.

Constrsaints:
1 <= T <= 100
1 <= |S|, |P| <= 104

Example:
Input:
2
aabaacaadaabaaba
aaaab
aabaacaadaabaaba
caada
Output:
No
Yes

Explanation:
Testcase 1: Given pattern is not found in the given string S.
Testcase 2: Given pattern is found in the given string S.
'''

def KMP(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    computeLPSArray(pat, M, lps)
    i, j = 0, 0
    while i < N:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        if j == M:
            return True
        elif i < N and txt[i] != pat[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
    return False
    
def computeLPSArray(pat, M, lps):
    prevLPS = 0
    i = 1
    while i < M:
        if pat[i] == pat[prevLPS]:
            prevLPS += 1
            lps[i] = prevLPS
            i += 1
        else:
            if prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS-1]

def main():
    t = int(input())
    while t:
        txt = str(input())
        pat = str(input())
        if KMP(pat, txt):
            print('Yes')
        else:
            print('No')
                
        t -= 1
        
if __name__ == '__main__':
    main()                                    
    
