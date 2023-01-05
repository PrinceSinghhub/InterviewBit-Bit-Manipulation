class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        Bin = bin(A)[2::]
        count = 0
        for i in Bin[::-1]:
            if i == '1':
                return count
            else:
                count+=1

ans = Solution()
print(ans.solve(10))
