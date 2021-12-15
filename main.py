class Rectangle:

  width = 0
  height = 0

  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height
  
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
      line = '*' * self.width
      lines = [line for _ in range(self.height)]
      pic = '\n'.join(lines)
      return pic + "\n"
          
  def get_amount_inside(self, shape):

    w = self.width // shape.width
    h = self.height // shape.height

    return w * h

  def __repr__(self):
    return "Rectangle(width=%r, height=%r)" %(self.width, self.height)

class Square(Rectangle):

  side = 0

  def __init__(self, side):
    self.height = side
    self.width = side

  def set_side(self, value):
    self.side = value
    self.width = value
    self.height = value
  
  def __repr__(self):
    return "Square(side=%r)" %(self.side)
