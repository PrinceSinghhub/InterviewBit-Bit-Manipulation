class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        ans = bin(A)[2::]
        return ans.count('1')


ans = Solution()
print(ans.numSetBits(10))