class Restangle:

    #Class level variables, shared by all the instances.
    rum_of_sides = 4
    rum_of_diagonals = 2

    def __init__(self, length, width): 

        #Instance level variables. Different for all the instances.
        #Sel.legth and self.width are instace variables here.
        self.length = length
        self.width = width

def are(self):
    """Método de instancia para calcular el área de instancia individual de rectángulo
    clase sobre la base de variables de instancia (self.legth and self.width).
    """
    return self.legth * self.width

def perimeter(self):
    """Instance method to calculate the perimeter of individual intance.
    """
    return 2 * (self.length + self.width)

@classmethod
def instantiate_square(cls, side):
    """Using class method as an alternate constructor.

    Args:
      Side (int) side of a square

    return:
      class_instance Rectangle class instance with both sides equal.

    """
    return cls(side, side)

@classmethod
def is_quadrilateral(cls):
    #class method to manipulate a class variable
    return True if cls.number_of_sides == 4 else False

@staticmethod
def rectangle_formulae():
    # Static method:
    # Display information related to a rectangle. But does not manipulate or work-upon
    # ani instance or class variables here.
    print("Area length X width")
    print("Perimeter: 2(length + width)")
    print("Diagonal: square_root(square_of_length + square_of_width)")
