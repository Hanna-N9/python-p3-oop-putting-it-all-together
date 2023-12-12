#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.size = size
        self.brand = brand
        
    def size(self):
        return self._size
     
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")