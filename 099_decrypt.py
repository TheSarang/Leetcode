class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        arr = []
        summ = 0
        if k != 0:
            for i in range(len(code)):
                for j in range(1, abs(k)+1):
                    if k > 0:
                        idx = i + j
                    elif k < 0:
                        idx = i - j
                    idx = (idx)%len(code)
                    summ += code[idx]
                arr.append(summ)
                summ = 0
        else:
            return [0 for _ in range(len(code))]
        return(arr)
