class ShapeFactory(object):
    """工厂类"""

    def getShape(self):
        return self.shape_name


class Circle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Circle"

    def draw(self):
        print('draw Circle')


class Square(ShapeFactory):
    def __init__(self):
        self.shape_name = "Square"

    def draw(self):
        print('draw Square')


class Rectangle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Retangle"

    def draw(self):
        print('draw Rectangle')


class Shape(object):
    """接口类，负责决定创建哪个ShapeFactory的子类"""

    def create(self, shape):
        if shape == 'Circle':
            return Circle()
        elif shape == 'Rectangle':
            return Rectangle()
        elif shape == 'Square':
            return Square()
        else:
            return None


fac = Shape()
obj = fac.create('Circle') # 选择接口
obj.draw()
obj.getShape()
