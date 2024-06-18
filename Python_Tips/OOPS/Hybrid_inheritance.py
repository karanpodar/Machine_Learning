"""
Hybrid inheritance when more than 1 type of inheritance is used.
Here we are using multilevel, multiple, heirarchial inheritance
"""

class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Base):
    pass

class Derived3(Derived1, Derived2):
    pass