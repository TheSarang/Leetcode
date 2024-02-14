class Solution:
def sortedSquares(self, A: List[int]) -> List[int]:
	list1 = []
	for i in A:
		list1.append(i*i)
		
	return sorted(list1, reverse=False)
