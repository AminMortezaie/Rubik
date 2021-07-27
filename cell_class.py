from color_class import Color
from place_class import Place

class Cell:
    color_array = []
    place = None
    def __init__(self, place, color):
        self.color_array = color.get_color_array()
        self.place = place.get_mode() 

    def get_place(self):
        return self.place
    
    def get_color_array(self):
        return self.color_array