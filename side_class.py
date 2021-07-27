class Side:
    front, back, top, bottom, right, left = 0,0,0,0,0,0
    def __init__(self, front, top, right):
        self.front, self.top, self.right = front, top, right
        self.set_sides()
    def side_reverse(self, color_num):
        if color_num==1:
            return 5 
        elif color_num==2:
            return 6
        elif color_num ==3:
            return 4
        elif color_num==4:
            return 3
        elif color_num==5:
            return 1
        elif color_num==6:
            return 2
    def set_sides(self):
        self.back = self.side_reverse(self.front)
        self.bottom = self.side_reverse(self.top)
        self.left = self.side_reverse(self.right)
    
         
            
            