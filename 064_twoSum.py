class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = -1
        middle = end // 2
        while True:
            if target == (numbers[start] + numbers[end]):
                return [start+1, len(numbers) + end + 1]
            elif target < (numbers[start] + numbers[end]):
                end -=1
            elif target > (numbers[start] + numbers[end]):
                start +=1
