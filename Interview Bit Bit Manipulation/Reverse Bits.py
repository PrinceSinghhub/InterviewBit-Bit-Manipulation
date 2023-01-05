class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        binary = bin(A)
        bitSize = 32

        reverse1 = binary[-1:1:-1]
        reverse1 = reverse1 + (bitSize - len(reverse1)) * '0'

        return (int(reverse1, 2))

ans = Solution()
print(ans.reverse(3))