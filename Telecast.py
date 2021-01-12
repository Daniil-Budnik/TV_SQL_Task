class Telecast():
      
  def __init__(self, id, name, rating, price):
    self.setID(id) 
    self.setName(name)
    self.setRating(rating)
    self.setPrice(price)

  def setID(self, id): self.__id = id
  def setName(self, value): self.__name = value
  def setRating(self, value): self.__rating = value
  def setPrice(self, value): self.__price = value

  def getID(self): return self.__id
  def getName(self): return self.__name
  def getRating(self): return self.__rating
  def getPrice(self): return self.__price

  def __str__(self):
        return "ID: {}\nНазвание: {}\nРейтинг: {}\nСтоимость минуты: {}".format(
            self.__id, self.__name, self.__rating, self.__price)

