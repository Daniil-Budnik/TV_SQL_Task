import Telecast as TL
import Client as CL
import Ad as AD

import json as JS

class Accounting:

    # ***************************************************************************

    def __init__(self, file_name=""):

        self.__clients = CL.ClientList()
        self.__telecasts = TL.TelecastList()
        self.__ads = AD.AdList()

        if file_name != "": self.read(file_name)

    # ***************************************************************************

    def read(self, file_name):

        with open(file_name) as Files: data = JS.load(Files)

        for item in data["clients"]:
            client = CL.Client(item["id"], item["companyName"], item["bankData"], item["phone"], item["contact"])
            self.__clients.append(client)

        for item in data["telecasts"]:
            telecast = TL.Telecast(item["id"], item["name"], item["rating"], item["price"])
            self.__telecasts.append(telecast)

        for item in data["ads"]:
            ad = AD.Ad(item["id"], self.__telecasts.getByID(item["telecast"]), self.__clients.getByID(item["client"]),item["date"], item["time"])
            self.__ads.append(ad)

    # ***************************************************************************

    def write(self, file_name):

      if file_name.endswith(".json"):

          clients = []
          for item in self.__clients:
              client = {
                  "id": item.getID(),
                  "companyName": item.getCompanyName(),
                  "bankData": item.getBankData(),
                  "phone": item.getPhone(),
                  "contact": item.getContact()
              }
              clients.append(client)

          telecasts = []
          for item in self.__telecasts:
              telecast = {
                  "id": item.getID(),                  
                  "name": item.getName(),              
                  "rating": item.getRating(),          
                  "price": item.getPrice()
              }
              telecasts.append(telecast)

          ads = []
          for item in self.__ads:
              ad = {
                  "id": item.getID(),
                  "telecast": item.getTelecast().getID(),
                  "client": item.getClient().getID(),
                  "date": item.getDate(),
                  "time": item.getTime()
              }
              ads.append(ad)

          data = {
              "clients": clients,
              "telecasts": telecasts,
              "ads": ads
          }

          with open(file_name, "w") as file_output: JS.dump(data, file_output)


     # ***************************************************************************

    def getArrClient(self): return self.__clients
    def getArrTelecasts(self): return self.__telecasts
    def getArrAds(self): return self.__ads

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

    def Clear(self):
        self.__clients.clear()
        self.__telecasts.clear()
        self.__ads.clear()

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

    def setCompanyName(self,ID, value): self.__clients[ID].setCompanyName(Value)
    def setBankData(self,ID, value): self.__clients[ID].setBankData(Value)
    def setPhone(self,ID, value): self.__clients[ID].setPhone(Value)
    def setContact(self, value): self.__clients[ID].setContact(Value)

    def getCompanyName(self,ID): return self.__clients[ID].getCompanyName()
    def getBankData(self,ID): return self.__clients[ID].getBankData()
    def getPhone(self,ID): return self.__clients[ID].getPhone()
    def getContact(self,ID): return self.__clients[ID].getContact()

    # ***************************************************************************

    def setName(self,ID, value): self.__telecasts[ID].setName(Value)
    def setRating(self,ID, value): self.__telecasts[ID].setRating(Value)
    def setPrice(self,ID, value): self.__telecasts[ID].setPrice(Value)

    def getName(self,ID): return self.__telecasts[ID].getName()
    def getRating(self,ID): return self.__telecasts[ID].getRating()
    def getPrice(self,ID): return self.__telecasts[ID].getPrice()
      
    # ***************************************************************************

    def setTelecast(self,ID, value): self.__ads[ID].setTelecast(Value)
    def setClient(self,ID, value): self.__ads[ID].setClient(Value)
    def setDate(self,ID, value): self.__ads[ID].setDate(Value)
    def setTime(self,ID, value): self.__ads[ID].setTime(Value)

    def getTelecast(self,ID): return self.__ads[ID].getTelecast()
    def getClient(self,ID): return self.__ads[ID].getClient()
    def getDate(self,ID): return self.__ads[ID].getDate()
    def getTime(self,ID): return self.__ads[ID].getTime()

    # ***************************************************************************
        
