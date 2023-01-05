class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if (A == 1):
            return 1
        if (A == 2):
            return 3

        cnt = 2
        ind = 2
        val = 2
        while (cnt < A):
            cnt += val
            if (cnt >= A):
                break
            cnt += val
            ind += 1
            if (cnt >= A):
                break
            val *= 2
            ind += 1

        temp = ["1" for _ in range(ind - 1)]
        # print("temp :",temp)
        # print("ind :",ind)
        diff = cnt - A
        if (diff == 0):
            ans = "1" + "".join(temp) + "1"
            return int(ans, 2)

        val //= 2
        ind = 0
        l = ind
        i = 0
        # print("diff :",diff)
        while (diff > 0):
            if (val <= diff):
                temp[i] = temp[l - 1 - i] = "0"
                diff -= val
            # else:
            #     temp[i]=temp[l-i-1]="1"
            i += 1
            val //= 2

        # for j in range (i,l//2):
        #     temp[j]=temp[l-j-1]="1"

        # print("temp :",temp)

        ans = "1" + "".join(temp) + "1"
        return int(ans, 2)

ans = Solution()
print(ans.solve(10))

