class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0 = N, 1 = E, 2 = S, 3 = W
        idx = 0 
        diretions = [[0,1],[1,0],[0,-1],[-1,0]]
        x, y = 0, 0
        
        for i in range(len(instructions)):
            step = instructions[i]
            if step == 'L':
                idx = (idx + 3) % 4
            elif step == 'R':
                idx = (idx + 1) % 4
            else:
                x += diretions[idx][0]
                y += diretions[idx][1]
        
        return (x == 0 and y == 0) or idx != 0
            
        
