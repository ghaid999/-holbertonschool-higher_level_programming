#!/usr/bin/env python3
"""Defind the abstract class Animal and it is supclass : Dog and Cat."""

from abc import ABC, abstractmethod

class Animal(ABC):
  """Defind the pase class Animal."""
  @abstractmethod
  def sound(self):
    """Reurn the sound of the pase class"""
    pass

class Dog(Animal):
  """Defind supclass Dog."""
  def sound(self):
    """Return the sound of supclass Dog"""
    return "Bark"
    
class Cat(Animal):
  """Defind supclass Cat."""
  def sound(self):
    """Return the sound of supclass Cat"""
    return "Meow"
