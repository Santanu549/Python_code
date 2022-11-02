# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 23:52:01 2022

@author: SANTANU
"""

class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class point3D(point):
     def position(self,z):
         self.z=z
     def __add__(self, other):
         z = self.z + other.z
         x = self.x + other.x
         y = self.y + other.y
         print(x, y, z)
     def sub(self, other):
         z = self.z - other.z
         x = self.x - other.x
         y = self.z - other.y
         print(x, y, z)
     def translation(self, other):
         z = self.z + other.z
         x = self.x + other.x
         y = self.y + other.y
         print(x, y, z)
     def reflex(self, other):
         self.x=-other.x
         self.y=-other.y
         self.z=-other.z
         print(self.x, self.y, self.z)

c=point3D(8,8)
c.position(8)
c1=point3D(8,8)
c1.position(8)
c1.__add__(c)
c1.sub(c)
c1.translation(c)
c1.reflex(c)