class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def _helper(stack):
            tempStack = []
            for i in range(len(stack)):
                if stack[i] != '#':
                    tempStack.append(stack[i])
                elif stack[i] == '#' and len(tempStack) != 0:
                    tempStack.pop()
            return tempStack
        
        stack_S = _helper(S)
        stack_T = _helper(T)
        
        if len(stack_S) != len(stack_T):
            return False
        else:
            for i in range(len(stack_S)):
                if stack_S[i] != stack_T[i]:
                    return False
                
        return True
