class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        Bin = bin(A)[2::]

        flip = ""
        for i in Bin:
            if i == "0":
                flip += "1"
            else:
                flip += "0"

        flip = str(int(flip))

        return int(flip, 2)

ans = Solution()
a = 560
print(ans.solve(a))