#!/usr/bin/env python3
"""containing Shape class and its inheritances"""
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
  """ Define the abstract class Shape. """
  @abstractmethod
  def area(self):
    """ methode area"""
    pass

  def perimeter(self):
     """ methode perimeter"""
    pass

class Circle(Shape):
  """create class Circle inhernt from Shape"""
  def __init__(self, radius):
    """ Initialization"""
    self.radius = abc(radius)

  def area(self):
    """ calcolate the area"""
    return pi * self.radius ** 2

  def perimeter(self):
     """ calcolate the perimeter"""
    return pi * self.radius * 2


class Rectangle(Shape):
   """create class Rectangle inhernt from Shape"""
  def __init__(self,width,height):
    """ Initialization"""
    self.width=width
    self.height=height

  def area(self):
    """ calcolate the area"""
    return self.width * self.height
    
  def perimeter(self):
    """ calcolate the perimeter"""
    return 2 * (self.width + self.height)

def shape_info (arg):
  """function that give the shape info """
  area = arg.area()
  perimeter = arg.perimeter()
  
  print("f Aera: {area}")
  print("f perimeter: {perimeter}")
  
