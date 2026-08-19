class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memory = {}
        # first check rows and columns
        for y in range(len(board)):
            memory = {}; # reset memory
            for x in range(len(board)):
                val = board[y][x];
                if val == ".": 
                    continue

                if val not in memory:
                    memory[val] = True
                else:
                    return False

        for y in range(len(board)):
            memory = {}; # reset memory
            for x in range(len(board)):
                val = board[x][y];
                if val == ".": 
                    continue

                if val not in memory:
                    memory[val] = True
                else:
                    return False      
        
        # now check the 3x3 boxes
        yIncrement = 3
        xIncrement = 3
        maxY = 9
        maxX = 9
        currentX, currentY = 0, 0
        while currentX < maxX and currentY < maxY:
            memory = {};
            for x in range(currentX, currentX+xIncrement):
                for y in range(currentY, currentY+yIncrement):
                    cellVal = board[x][y]
                    if cellVal == ".": 
                        continue

                    if cellVal not in memory:
                        memory[cellVal] = True
                    else:
                        return False 
            currentX += xIncrement
            if currentX == maxX:
                currentX = 0;
                currentY += yIncrement;
        return True


        
        
            
