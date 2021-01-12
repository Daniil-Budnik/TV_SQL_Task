import Telecast as TL
import Client as CL
import Ad as AD

class DataList(list):
    def getByID(self, id):
          for item in self:
                if item.getID() == id: return item
          else: return None 

class DataBaseMain():

    def __init__(self): 
        self.__clients =    DataList()
        self.__telecasts =  DataList()
        self.__ads =        DataList()

    # ***************************************************************************

    def ImportDataBase(self,DataBaseExemplar):
        NewDataBase = DataBaseExemplar.getDataBase()
        self.setDataBase(NewDataBase)

    def getDataBase(self): return {"Client" : self.__clients, "Telecasts" : self.__telecasts, "Ads" : self.__ads}

    def setDataBase(self,DataBaseArr):
        self.__clients =     DataBaseArr["Client"]
        self.__telecasts =      DataBaseArr["Telecasts"]
        self.__ads =   DataBaseArr["Ads"]

    # ***************************************************************************

    def Clear(self):
        self.__clients.clear()
        self.__telecasts.clear()
        self.__ads.clear()

    # ***************************************************************************

    def addClients(self,value): 
        for ITEM in self.__clients:
           if(ITEM.getID() == value.getID()) : return 0
        self.__clients.append(value)

    def addTelecasts(self,value): 
        for ITEM in self.__telecasts:
           if(ITEM.getID() == value.getID()) : return 0
        self.__telecasts.append(value)

    def addAds(self,value): 
        for ITEM in self.__ads:
           if(ITEM.getID() == value.getID()) : return 0
        self.__ads.append(value)
                             
    # ***************************************************************************

    def removeTelecasts(self,ID): 
        N = 0
        for ITEM in self.__telecasts:
            if(ITEM.getID() == ID): 
                for I in self.__ads:
                    if(I.getTelecast() == ITEM):
                        print("ERROR: Ошибка удаления")
                        return 0
                self.__Client.pop(N)
                return 0
            N+=1
       
    def removeClient(self,ID): 
        N = 0
        for ITEM in self.__clients:
            if(ITEM.getID() == ID):
                for I in self.__ads:
                    if(I.getClient() == ITEM):
                        print("ERROR: Ошибка удаления")
                        return 0
                self.__Route.pop(N)
                return 0
            N+=1

    def removeAd(self, ID): 
        N = 0
        for ITEM in self.__ads:
            if(ITEM.getID() == ID): 
                self.__Vouchers.pop(N)
                return 0
            N+=1

     # ***************************************************************************

    def setCompanyName(self,ID, value): self.__clients[ID].setCompanyName(value)
    def setBankData(self,ID, value): self.__clients[ID].setBankData(value)
    def setPhone(self,ID, value): self.__clients[ID].setPhone(value)
    def setContact(self, value): self.__clients[ID].setContact(value)

    def getCompanyName(self,ID): return self.__clients[ID].getCompanyName()
    def getBankData(self,ID): return self.__clients[ID].getBankData()
    def getPhone(self,ID): return self.__clients[ID].getPhone()
    def getContact(self,ID): return self.__clients[ID].getContact()

    # ***************************************************************************

    def setName(self,ID, value): self.__telecasts[ID].setName(value)
    def setRating(self,ID, value): self.__telecasts[ID].setRating(value)
    def setPrice(self,ID, value): self.__telecasts[ID].setPrice(value)

    def getName(self,ID): return self.__telecasts[ID].getName()
    def getRating(self,ID): return self.__telecasts[ID].getRating()
    def getPrice(self,ID): return self.__telecasts[ID].getPrice()
      
    # ***************************************************************************

    def setTelecast(self,ID, value): self.__ads[ID].setTelecast(value)
    def setClient(self,ID, value): self.__ads[ID].setClient(value)
    def setDate(self,ID, value): self.__ads[ID].setDate(value)
    def setTime(self,ID, value): self.__ads[ID].setTime(value)

    def getTelecast(self,ID): return self.__ads[ID].getTelecast()
    def getClient(self,ID): return self.__ads[ID].getClient()
    def getDate(self,ID): return self.__ads[ID].getDate()
    def getTime(self,ID): return self.__ads[ID].getTime()

    # ***************************************************************************

    def getArrClient(self): return self.__clients
    def getArrTelecasts(self): return self.__telecasts
    def getArrAds(self): return self.__ads
