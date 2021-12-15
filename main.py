class Rectangle:

  width = 0
  height = 0

  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, value):
    self.width = value
    
  def set_height(self, value):
    self.height = value

  def get_area(self):
    self.area = self.width * self.height
    return self.area

  def get_perimeter(self):
    self.perimeter= (2 * self.width + 2 * self.height)
    return self.perimeter

  def get_diagonal(self):
    self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return self.diagonal

  def get_picture(self):
    self.string1 = "*" * (self.width)

    if self.height > 50:
      print("Too big for picture.")
      
    elif self.width > 50:
      print("Too big for picture.")

    else:
          i=0
          while i<self.height:
            print(self.string1)
            i += 1
          
  def get_amount_inside(self):
    self.amount_inside = (self.width * self.height) / (self.area)

  def __repr__(self):
    return "Rectangle(width=%r, height=%r)" %(self.width, self.height)

class Square:

  side = 0

  def __init__(self, side):
    self.side = side
    self.height = Rectangle.height
    self.width = Rectangle.width

  def set_side(self, value):
    self.side = value
  
  def set_width(self, value):
    self.width = value
    self.side = value
  
  def set_height(self, value):
    self.height = value
    self.side = value
  
  def get_area(self):
    self.area = self.side * self.side
    return self.area

  def get_diagonal(self):
    self.diagonal = (self.side ** 2 + self.side ** 2) ** .5
    return self.diagonal
  
  def get_picture(self):
    self.string1 = "*" * (self.side)

    if self.side > 50:
      print("Too big for picture.")

    else:
          i=0
          while i<self.side:
            print(self.string1)
            i += 1

  def __repr__(self):
    return "Square(side=%r)" %(self.side)

rect = Rectangle(10,5)
print(rect.height)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
rect.get_picture()

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside())

# sq = shape_calculator.Square(9)
# print(sq.get_area())
# sq.set_side(4)
# 
# print(sq)
# 

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))

#Sırada kareye fonksiyonları geçirmek var

#Get amount inside kaldı bir tek
