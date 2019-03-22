"""
models the products at Acme corp.
"""

"""
imports
"""
import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 id=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.id = id
       
    def stealability(self):
        ratio = self.price/self.weight
        if ratio < 0.5:
            return 'not so stealable...'
        if ratio >= 0.5 and ratio < 1:
            return 'kinda stealable'
        if ratio >= 1:
            return 'very stealable!'
          
    def explodability(self):
        product = self.flammability*self.weight
        if product < 10:
          return '...fizzle.'
        if product >= 10 and product < 50:
          return '...boom!'
        if product > 50:
          return '...BABOOM!!'
    
    
class BoxingGlove(Product):
    '''
    override default weight and interaction with explodability
    '''
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 id=random.randint(100000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.id = id
        
    def punch(self):
        if self.weight < 5:
            return 'that tickles!'
        if self.weight >= 5 and self.weight < 15:
            return 'hey, that hurt!'
        if self.weight > 15:
            return 'OUCH!'
        
     def explodability(self):
        return "it's a glove."
