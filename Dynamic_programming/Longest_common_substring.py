class Solution:

    def LongestCommonSubstring(self, s1: str, s2:str) -> str:

        m , n = len(s1), len(s2)
        LCS = [[0 for i in range(n+1)] for j in range(m+1)]

        max_length = 0
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    LCS[i+1][j+1] = 1 + LCS[i][j]
                    max_length = max(max_length,LCS[i+1][j+1])

        return max_length
    
    def printLongestCommonSubstring(self, s1:str, s2:str) ->None:

        m , n = len(s1), len(s2)
        LCS = [[0 for i in range(n+1)] for j in range(m+1)]

        max_length = 0
        LCS_i , LCS_j = 0 , 0
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    LCS[i+1][j+1] = 1 + LCS[i][j]
                    if LCS[i+1][j+1] > max_length:
                        max_length = max(max_length,LCS[i+1][j+1])
                        LCS_i , LCS_j = i , j


        while LCS_i > 0 and LCS_j > 0 and LCS[LCS_i+1][LCS_j+1] > 0:
            print(s1[LCS_i],end='')
            LCS_i -= 1
            LCS_j -= 1
    

if __name__ == "__main__":
    s1 = "abcdaf"
    s2 = "acbcf"
    print(s1,s2)
    s = Solution()
    print(s.LongestCommonSubstring(s1,s2))
    s.printLongestCommonSubstring(s1,s2)