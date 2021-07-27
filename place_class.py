class Place:
    mode = 0
    def __init__(self, mode):
        self.mode = mode
        if mode == 3:
            self.place_name = "corner"  
        elif mode ==1 :
            self.place_name = "one-center"
        elif mode ==2 :
            self.place_name = "center"
        
    def get_mode(self):
        return self.mode
    
    def get_place_name(self):
        return self.place_name
    