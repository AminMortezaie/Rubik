from color_class import Color
from place_class import Place
from side_class import Side
from cell_class import Cell


class Rubik:
    cell_array = []
    def __init__(self):
    #installation
        side_obj = Side(1,2,3)
        self.make_rubik()
          
        
        
    def make_rubik(self):
        self.make_one_centers()
        self.make_centers()
        self.make_corners()
        
        
                
    def make_one_centers(self):
        #make one-centers
        for color in range(1,7):
            place_obj = Place(1)
            color_obj = Color(place_obj,color,0,0)
            # print(color)
            cell_obj = Cell(place_obj, color_obj)
            self.cell_array.append(cell_obj)
    
    def make_centers(self):
        #make centers
        seen = []
        place_obj = Place(2)
        temp = Color(place_obj,1,1,0)
        for color1 in range(1,7):
            arr = temp.get_probable_colors(color1)
            for color2 in arr: 
                if str(color1)+str(color2) and str(color2)+str(color1) not in seen:
                    seen.append(str(color1)+str(color2))
                    seen.append(str(color2)+str(color1))
                    color_obj = Color(place_obj,color1,color2,0)
                    cell_obj = Cell(place_obj, color_obj)
                    self.cell_array.append(cell_obj)
        # for ele in self.cell_array:
        #     print(ele.get_color_array())
    
    def make_corners(self):
        #make corners
        seen = []
        place_obj = Place(3)
        temp = Color(place_obj,1,1,1)
        for color1 in range(1,7):
            arr = temp.get_probable_colors(color1)
            for color2 in arr: 
                arr1 = temp.get_probable_colors(color2)
                s ={}
                s = set(arr) & set(arr1)
                # s.remove(color2)
                for color3 in list(s):
                    if str(color1)+str(color2)+str(color3) and str(color1)+str(color3)+str(color2) and str(color2)+str(color1)+str(color3) and str(color2)+str(color3)+str(color1) and str(color3)+str(color1)+str(color2) and str(color3)+str(color2)+str(color1) not in seen:
                        seen.append(str(color1)+str(color2)+str(color3))
                        seen.append(str(color1)+str(color3)+str(color2))
                        seen.append(str(color2)+str(color1)+str(color3))
                        seen.append(str(color2)+str(color3)+str(color1))
                        seen.append(str(color3)+str(color1)+str(color2))
                        seen.append(str(color3)+str(color2)+str(color1))
                        
                        color_obj = Color(place_obj,color1,color2,color3)
                        cell_obj = Cell(place_obj, color_obj)
                        self.cell_array.append(cell_obj)
        c=0 
        for ele in self.cell_array:
            # c+=1
            # print(c)
            print(ele.get_color_array())
            

        
        
    
    
obj = Rubik()