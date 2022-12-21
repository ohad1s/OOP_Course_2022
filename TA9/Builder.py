"""
The builder design pattern is a creational design pattern that allows you to
construct complex objects step by step. It can be particularly useful when the process of
constructing an object is complex, or when you need to create different variations of an object using the same construction process.
"""
# The Car class represents the final product that we want to build.
# It has a number of fields that can be set, such as make, model, year, etc.
class Car:
  def __init__(self):
    self.make = None
    self.model = None
    self.year = None
    self.color = None
    self.engine = None
    self.transmission = None

  def __str__(self):
    return f'{self.year} {self.make} {self.model} ({self.engine}, {self.transmission}, {self.color})'

# The CarBuilder class is a builder that knows how to create a Car object.
# It has a number of methods that can be used to set the various fields of the Car object.
class CarBuilder:
  def __init__(self):
    self.car = Car()

  def set_make(self, make):
    self.car.make = make
    return self

  def set_model(self, model):
    self.car.model = model
    return self

  def set_year(self, year):
    self.car.year = year
    return self

  def set_color(self, color):
    self.car.color = color
    return self

  def set_engine(self, engine):
    self.car.engine = engine
    return self

  def set_transmission(self, transmission):
    self.car.transmission = transmission
    return self

  def build(self):
    return self.car

# The CarDirector class is a director that knows how to create a specific type of Car object using the CarBuilder.
# In this case, it knows how to create a sports car.
class CarDirector:
  def __init__(self, builder):
    self.builder = builder

  def build_sports_car(self):
    return self.builder.set_make('Porsche').set_model('911').set_year(2020).set_color('red').set_engine('V6').set_transmission('manual').build()


# Now we can use the CarDirector to build a sports car.
builder = CarBuilder()
director = CarDirector(builder)
car = director.build_sports_car()
print(car)  # Output: 2020 Porsche 911 (V6, manual, red)
