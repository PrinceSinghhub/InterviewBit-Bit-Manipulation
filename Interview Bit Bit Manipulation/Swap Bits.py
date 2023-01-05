class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, n, p, q):

        if (((n & (1 << p-1)) >> p-1) ^ ((n & (1 << q-1)) >> q-1)):

            n ^= (1 << p-1)
            n ^= (1 << q-1)


        return n

ans = Solution()
a=10;b=20;
c=30
print(ans.solve(a,b,c))