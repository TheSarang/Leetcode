class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TC: O(n)^2
        # SC: O(n)

        n = len(nums)
        nums.sort()
        ans = []
        mySet = set()

        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    mySet.add(tuple(temp))
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                elif total > 0:
                    k -= 1

        for x in mySet:
            ans.append(list(x))
        return ans
