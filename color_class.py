from place_class import Place
class Color:
    c1 = "white"
    c2 = "blue"
    c3 = "red"
    c4 = "orange"
    c5 = "yellow"
    c6 = "green"
    color_array = []
    place = None
    def __init__(self, place, color1=0, color2=0, color3=0):
        self.place = Place(place.get_mode())
        self.mode = place.get_mode()
        # print(place.place_name)
        self.color_array = self.set_color(color1,color2,color3)
    
        
    
    def set_color(self, color1, color2, color3):
        arr =[]
        mode = self.mode
        if mode ==1:
            if color2 ==0 and color3 ==0:
                arr.append(self.color(color1))
                arr.append(None)
                arr.append(None)
                return arr
            else:
                print("Wrong variables!")
                return -1
        if mode ==2:
            if color3 ==0 and color1!=0 and color2!=0:
                arr.append(self.color(color1))
                arr.append(self.color(color2))
                arr.append(None)
                return arr
            else:
                print("Wrong variables!")
                return -1
        if mode ==3:
            if color1 !=0 and color2!=0 and color3!=0:    
                arr.append(self.color(color1))
                arr.append(self.color(color2))
                arr.append(self.color(color3))
                return arr
            else:
                print("Wrong variables!")
                return -1
        
    def color(self, color_num):
        if color_num == 0:
            return None
        elif color_num == 1:
            return self.c1
        elif color_num == 2:
            return self.c2
        elif color_num == 3:
            return self.c3
        elif color_num == 4:
            return self.c4
        elif color_num == 5:
            return self.c5
        elif color_num == 6:
            return self.c6
        
    def reverse_color(self, color_num):
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
    
    def get_probable_colors(self,color_num):
        arr = []
        reverse_color = self.reverse_color(color_num)
        for i in range(1,7):
            if i == reverse_color or i==color_num:
                pass
            else:
                arr.append(i)
        return arr
    
    def get_color_array(self):
        if self.color_array != [None, None, None]:
            return self.color_array
        else: 
            print("No color seted!")
    
