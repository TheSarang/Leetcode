class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for i in logs:
            if i.split(" ")[1].isdigit():
                digit_logs.append(i)
            else:
                letter_logs.append(i)
                
        letter_logs.sort(key = lambda x:x.split(" ")[0])
        letter_logs.sort(key = lambda x:x.split(" ")[1:])
        letter_logs.extend(digit_logs)
        return letter_logs
