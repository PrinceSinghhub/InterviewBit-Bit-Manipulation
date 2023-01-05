class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):

        res = 0

        for i in A:
            res = res ^ i

        return res


ans = Solution()
A = [1, 2, 2, 3, 1]
print(ans.singleNumber(A))