class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        pre_op = "+"
        s += '+'
        for i in range(len(s)):
            cur = s[i]
            if cur.isdigit():
                num = 10 * num + int(cur)
            elif cur == ' ':
                continue
            else:
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    temp = stack.pop()
                    stack.append(temp*num)
                else:
                    temp = stack.pop()
                    stack.append(int(temp/num))
                num = 0
                pre_op = cur
        return sum(stack)
