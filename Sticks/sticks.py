# sticks itself
class sticks:
    def __init__(self, size):
        self.size = size
        self.sticks = int((1+size)/2*size)
        board = []
        # add row index list
        temp = []
        for i in range(size+1):
            if i == 0:
                temp += " "
            else:
                temp.extend(str(i-1))
        board.append(temp)
        # add the rest of the board
        i = 0
        for i in range(size):
            temp = []
            temp.extend(str(i))
            j = i+1
            while j>0:
                temp.extend(str(1))
                j -= 1    
            board.append(temp)
            i += 1
        self.board = board 
        
    def render_sticks(self):
        print("Remaining Sticks: "+str(self.sticks))
        for row in self.board:
            print(*row, sep=" ")
    
    def remove_sticks(self, col, row, amt):
        # checking if input is digit
        if col.isdigit() == False or row.isdigit() == False or amt.isdigit() == False:
            return True
        
        c = int(col)
        r = int(row)
        a = int(amt)

        def check_range(c, r, a): # to check if numbers inputed are in range
            if r >= self.size:
                return True
            if c > r:
                return True
            if a > r + 1:
                return True
            if a > ((r-c)+1):
                return True
            return False
        
        def check_valid(c, r, a): # to check if the input is valid
            temp_c = c + 1
            temp_r = r + 1
            temp_a = a
            while temp_a != 0:
                if self.board[temp_r][temp_c] == "-":
                    return True
                temp_c += 1
                temp_a -= 1
            return False
        
        # checking input        
        if check_range(c, r, a) == True:
            return True
        if check_valid(c, r, a) == True:
            return True
    
        # removing sticks
        c += 1 
        r += 1
        self.sticks -= a
        while a != 0:
            self.board[r][c]="-"
            c += 1
            a -= 1



