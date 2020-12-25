class Client():

  def __init__(self, id, companyName, bankData, phone, contact):
    self.setID(id)    
    self.setCompanyName(companyName)
    self.setBankData(bankData)
    self.setPhone(phone)
    self.setContact(contact)

  def setID(self, id): self.__id = id
  def setCompanyName(self, value): self.__companyName = value
  def setBankData(self, value): self.__bankData = value
  def setPhone(self, value): self.__phone = value
  def setContact(self, value): self.__contact = value

  def getID(self): return self.__id
  def getCompanyName(self): return self.__companyName
  def getBankData(self): return self.__bankData
  def getPhone(self): return self.__phone
  def getContact(self): return self.__contact

  def __str__(self):
        return "ID: {}\nНазвание: {}\nБанковские реквизиты: {}\nТелефон: {}\nКонтактное лицо: {} ".format(
            self.__id, self.__companyName, self.__bankData, self.__phone, self.__contact)

class ClientList(list):
  def getByID(self, id):
        for item in self:
              if item.getID() == id: return item
        else: return None 