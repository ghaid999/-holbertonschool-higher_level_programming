#!/usr/bin/env python3
""" Dragon class with mixins"""


class SwimMixin:
  """ class SwimMixin."""
  def swim(self):
    print( "The creature swims!")

class FlyMixin:
  """ class FlyMixin."""
  def fly(self):
    prints("The creature flies!")

class Dragon(SwimMixin,FlyMixin):
  """ class Dragon."""
  def rora(self):
    prints("The dragon roars!")
  
