import Telecast as TL
import Client as CL

class Ad():
  __id = int
  __telecast = TL.Telecast
  __client = CL.Client
  __date = str
  __time = int

  def __init__(self, id, telecast, client, date, time):
    self.setID(id)
    self.setTelecast(telecast)
    self.setClient(client)
    self.setDate(date)
    self.setTime(time)

  def setID(self, id): self.__id = id
  def setTelecast(self, value): self.__telecast = value
  def setClient(self, value): self.__client = value
  def setDate(self, value): self.__date = value
  def setTime(self, value): self.__time = value

  def getID(self): return self.__id
  def getTelecast(self): return self.__telecast
  def getClient(self): return self.__client
  def getDate(self): return self.__date
  def getTime(self): return self.__time

  def __str__(self):
        return "ID: {}\nПередача: {}\nКлиент: {}\nДата показа: {}\nДлительность в минутах: {} ".format(
            self.__id, self.__telecast, self.__client, self.__date, self.__time)
