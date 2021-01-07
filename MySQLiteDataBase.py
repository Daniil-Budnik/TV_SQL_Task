import Telecast as TL
import Client as CL
import Ad as AD

import sqlite3 as SQL

class DataBaseSQL:

    def __init__(self, file_name=""): 
        self.__clients = CL.ClientList()
        self.__telecasts = TL.TelecastList()
        self.__ads = AD.AdList()

        if file_name != "": self.read(file_name)


    # ***************************************************************************

    def read(self,file_name):

        DataBase = SQL.connect(file_name)
        SQLite = DataBase.cursor()

        for ITEM in SQLite.execute("SELECT * FROM Telecast"):     
            C = TL.Telecast(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3])
            self.__telecasts.append(C)
        
        for ITEM in SQLite.execute("SELECT * FROM Client"):      
            C = CL.Client(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3],ITEM[4])
            self.__clients.append(C)
        
        for ITEM in SQLite.execute("SELECT * FROM Ad"):   
            C = AD.Ad(int(ITEM[0]),self.__telecasts.getByID(int(ITEM[1])),self.__clients.getByID(int(ITEM[2])),ITEM[3],ITEM[4])
            self.__ads.append(C)

    # ***************************************************************************

    def write(self,file_name):

        DataBase = SQL.connect(file_name)
        SQLite = DataBase.cursor()

        SQLite.execute("""CREATE TABLE IF NOT EXISTS Telecast (ID INT, name TEXT, rating TEXT, price TEXT)""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Client (ID INT, companyName TEXT, bankData TEXT, phone TEXT, contact TEXT)""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Ad (ID INT, telecast INT, client INT, date TEXT, time TEXT)""")

        DataBase.commit()

        Arr_T = [ [
            self.__telecasts[I].getID(),
            self.__telecasts[I].getName(),
            self.__telecasts[I].getRating(),
            self.__telecasts[I].getPrice(), 
            ] for I in range(len(self.__telecasts)) ]
        
        print(self.__clients[0])
        Arr_C = [ [
            self.__clients[I].getID(),
            self.__clients[I].getCompanyName(),
            self.__clients[I].getBankData(),
            self.__clients[I].getPhone(), 
            self.__clients[I].getContact(),
            ] for I in range(len(self.__clients)) ]

        
        Arr_A = [ [
            self.__ads[I].getID(),
            self.__ads[I].getTelecast().getID(),
            self.__ads[I].getClient().getID(),
            self.__ads[I].getDate(), 
            self.__ads[I].getTime(),
            ] for I in range(len(self.__ads)) ]

        for ID in range(len(Arr_T)):

            SQLite.execute(f"SELECT ID FROM Telecast WHERE ID = {Arr_T[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Telecast VALUES ( {Arr_T[ID][0]}, '{Arr_T[ID][1]}', '{Arr_T[ID][2]}', '{Arr_T[ID][3]}')")
            DataBase.commit()

        for ID in range(len(Arr_C)):

            SQLite.execute(f"SELECT ID FROM Client WHERE ID = {Arr_C[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Client VALUES ( {Arr_C[ID][0]}, '{Arr_C[ID][1]}', '{Arr_C[ID][2]}', '{Arr_C[ID][3]}', '{Arr_C[ID][4]}')")
            DataBase.commit()

        for ID in range(len(Arr_A)):

            SQLite.execute(f"SELECT ID FROM Ad WHERE ID = {Arr_A[ID][0]}")
            if SQLite.fetchone() is None:
                SQLite.execute(f"INSERT INTO Ad VALUES ( {Arr_A[ID][0]}, {Arr_A[ID][1]}, {Arr_A[ID][2]}, '{Arr_A[ID][3]}', '{Arr_A[ID][4]}')")
            DataBase.commit()
    
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

def GenTestFile(File): 

    DataBase = SQL.connect(File)
    SQLite = DataBase.cursor()

    Arr_T = [
        [1, "Вечерний Ургант", 10, 500000],
        [2, "На приеме у Шевцова", 7, 100000],
        [3, "Камеди Клаб", 5, 50000]]
    
    Arr_C = [
        [1, "Банк", "54805460736034", 89271653040, "Дмитрий Александрович"],
        [2, "Кит Медиа", "19805460736986", 89654738219, "Павел Павлович"],
        [3, "Газпром", "90805189841135", 89169875565, "Иван Иванович"] ]
    
    Arr_A = [
        [1, 1, 3, "20.10.2020", 3],
        [2, 2, 1, "20.10.2021", 4],
        [3, 3, 2, "20.10.2022", 5]]

    SQLite.execute("""CREATE TABLE IF NOT EXISTS Telecast (ID INT, name TEXT, rating TEXT, price TEXT)""")
    SQLite.execute("""CREATE TABLE IF NOT EXISTS Client (ID INT, companyName TEXT, bankData TEXT, phone TEXT, contact TEXT)""")
    SQLite.execute("""CREATE TABLE IF NOT EXISTS Ad (ID INT, telecast INT, client INT, date TEXT, time TEXT)""")

    DataBase.commit()

    for ID in range(3):

        SQLite.execute(f"SELECT ID FROM Telecast WHERE ID = {Arr_T[ID][0]}")
        if SQLite.fetchone() is None:
            SQLite.execute(f"INSERT INTO Telecast VALUES ( {Arr_T[ID][0]}, '{Arr_T[ID][1]}', '{Arr_T[ID][2]}', '{Arr_T[ID][3]}')")
        DataBase.commit()

        SQLite.execute(f"SELECT ID FROM Client WHERE ID = {Arr_C[ID][0]}")
        if SQLite.fetchone() is None:
            SQLite.execute(f"INSERT INTO Client VALUES ( {Arr_C[ID][0]}, '{Arr_C[ID][1]}', '{Arr_C[ID][2]}', '{Arr_C[ID][3]}', '{Arr_C[ID][4]}')")
        DataBase.commit()

        SQLite.execute(f"SELECT ID FROM Ad WHERE ID = {Arr_A[ID][0]}")
        if SQLite.fetchone() is None:
            SQLite.execute(f"INSERT INTO Ad VALUES ( {Arr_A[ID][0]}, {Arr_A[ID][1]}, {Arr_A[ID][2]}, '{Arr_A[ID][3]}', '{Arr_A[ID][4]}')")
        DataBase.commit()
