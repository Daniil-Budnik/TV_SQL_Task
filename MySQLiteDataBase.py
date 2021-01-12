import Telecast as TL
import Client as CL
import Ad as AD

from DataBaseMain import DataBaseMain

import sqlite3 as SQL



class DataBaseSQL(DataBaseMain):

    def read(self,file_name):

        DataBase = SQL.connect(file_name)
        SQLite = DataBase.cursor()

        for ITEM in SQLite.execute("SELECT * FROM Telecast"):     
            C = TL.Telecast(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3])
            self._DataBaseMain__telecasts.append(C)
        
        for ITEM in SQLite.execute("SELECT * FROM Client"):      
            C = CL.Client(int(ITEM[0]),ITEM[1],ITEM[2],ITEM[3],ITEM[4])
            self._DataBaseMain__clients.append(C)
        
        for ITEM in SQLite.execute("SELECT * FROM Ad"):   
            C = AD.Ad(int(ITEM[0]),self._DataBaseMain__telecasts.getByID(int(ITEM[1])),self._DataBaseMain__clients.getByID(int(ITEM[2])),ITEM[3],ITEM[4])
            self._DataBaseMain__ads.append(C)

    # ***************************************************************************

    def write(self,file_name):

        DataBase = SQL.connect(file_name)
        SQLite = DataBase.cursor()

        SQLite.execute("""CREATE TABLE IF NOT EXISTS Telecast (ID INT, name TEXT, rating TEXT, price TEXT)""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Client (ID INT, companyName TEXT, bankData TEXT, phone TEXT, contact TEXT)""")
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Ad (ID INT, telecast INT, client INT, date TEXT, time TEXT)""")

        DataBase.commit()

        Arr_T = [ [
            self._DataBaseMain__telecasts[I].getID(),
            self._DataBaseMain__telecasts[I].getName(),
            self._DataBaseMain__telecasts[I].getRating(),
            self._DataBaseMain__telecasts[I].getPrice(), 
            ] for I in range(len(self._DataBaseMain__telecasts)) ]
        
        Arr_C = [ [
            self._DataBaseMain__clients[I].getID(),
            self._DataBaseMain__clients[I].getCompanyName(),
            self._DataBaseMain__clients[I].getBankData(),
            self._DataBaseMain__clients[I].getPhone(), 
            self._DataBaseMain__clients[I].getContact(),
            ] for I in range(len(self._DataBaseMain__clients)) ]
        
        Arr_A = [ [
            self._DataBaseMain__ads[I].getID(),
            self._DataBaseMain__ads[I].getTelecast().getID(),
            self._DataBaseMain__ads[I].getClient().getID(),
            self._DataBaseMain__ads[I].getDate(), 
            self._DataBaseMain__ads[I].getTime(),
            ] for I in range(len(self._DataBaseMain__ads)) ]

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