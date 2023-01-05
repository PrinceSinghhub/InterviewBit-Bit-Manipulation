class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        if not A: return
        ones = 0
        twos = 0
        for i in range(len(A)):
            twos = twos | (ones & A[i])
            ones = ones ^ A[i]
            not_threes = ~(ones & twos)
            ones = ones & not_threes
            twos = twos & not_threes
        return ones

ans = Solution()
A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
print(ans.singleNumber(A))