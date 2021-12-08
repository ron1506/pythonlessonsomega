import random


class Robot(object):
    def __int__(self, pos_x=0, pos_y=0, color="black", lang='HEB', takin=True, dance_list=[], energy=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.lang = lang
        self.takin = takin
        self.dance_list = dance_list
        self.energy = energy

    def move(self):
        self.pos_x += random.randint(-1, 1)
        self.pos_y += random.randint(-1, 1)


    def __str__(self):
        pass