import Telecast as TL
import Client as CL
import Ad as AD
import Accounting as AC
import MySQLiteDataBase as MyDB

# ***************************************************************************

def Task_1():

    Arr_T = [
      TL.Telecast(1, "Вечерний Ургант", 10, 500000),
      TL.Telecast(2, "На приеме у Шевцова", 7, 100000),
      TL.Telecast(3, "Камеди Клаб", 5, 50000)
    ]
    
    Arr_C = [
      CL.Client(1, "Банк", "54805460736034", 89271653040, "Дмитрий Александрович"),
      CL.Client(2, "Кит Медиа", "19805460736986", 89654738219, "Павел Павлович"),
      CL.Client(3, "Газпром", "90805189841135", 89169875565, "Иван Иванович")
    ]
    
    Arr_A = [
        AD.Ad(1, Arr_T[0], Arr_C[2], "20.10.2020", 3),
        AD.Ad(2, Arr_T[1], Arr_C[0], "20.10.2021", 4),
        AD.Ad(3, Arr_T[2], Arr_C[1], "20.10.2022", 5)
        ]

    print("\nПередачи:\n")
    for ITEM in Arr_T: print(ITEM,'\n')
    
    print("\nКлиенты:\n")
    for ITEM in Arr_C: print(ITEM,'\n')
    
    print("\nРеклама:\n")
    for ITEM in Arr_A: print(ITEM,'\n')

# ***************************************************************************

def Task_2():

    DB = AC.Accounting("data.json")

    print("\nПередачи:\n")
    for ITEM in DB.getArrTelecasts(): print(ITEM,'\n')
    
    print("\nКлиенты:\n")
    for ITEM in DB.getArrClient(): print(ITEM,'\n')
    
    print("\nРеклама:\n")
    for ITEM in DB.getArrAds(): print(ITEM,'\n')

    dTL = TL.Telecast(3,"ЯРИК","Большой",5000)
    dCL = CL.Client(3,"РосГосСтрах","Банковские данный","88005553555","Безконтактный")
    dAD = AD.Ad(3,dTL,dCL,"Вчера","Навсегда")

    DB.addTelecasts(dTL)
    DB.addClients(dCL)
    DB.addAds(dAD)

    DB.write("new.json")

    DB.Clear()

    DB.read("new.json")

    print("НОВЫЙ ФАЙЛ !!! ---------------------------")

    print("\nПередачи:\n")
    for ITEM in DB.getArrTelecasts(): print(ITEM,'\n')
    
    print("\nКлиенты:\n")
    for ITEM in DB.getArrClient(): print(ITEM,'\n')
    
    print("\nРеклама:\n")
    for ITEM in DB.getArrAds(): print(ITEM,'\n')


# ***************************************************************************

def Task_3(): 
    MyDB.GenTestFile("DataBase.db")

    DB = MyDB.DataBaseSQL("DataBase.db")

    print("\nПередачи:\n")
    for ITEM in DB.getArrTelecasts(): print(ITEM,'\n')
    
    print("\nКлиенты:\n")
    for ITEM in DB.getArrClient(): print(ITEM,'\n')
    
    print("\nРеклама:\n")
    for ITEM in DB.getArrAds(): print(ITEM,'\n')

    dTL = TL.Telecast(4,"ЯРИК","Большой",5000)
    dCL = CL.Client(4,"РосГосСтрах","Банковские данный","88005553555","Безконтактный")
    dAD = AD.Ad(4,dTL,dCL,"Вчера","Навсегда")

    DB.addTelecasts(dTL)
    DB.addClients(dCL)
    DB.addAds(dAD)

    DB.write("new.db")
    
    DB.Clear()
    
    DB.read("new.db")
    
    print("НОВЫЙ ФАЙЛ !!! ---------------------------")
    
    print("\nПередачи:\n")
    for ITEM in DB.getArrTelecasts(): print(ITEM,'\n')
    
    print("\nКлиенты:\n")
    for ITEM in DB.getArrClient(): print(ITEM,'\n')
    
    print("\nРеклама:\n")
    for ITEM in DB.getArrAds(): print(ITEM,'\n')

# ***************************************************************************

def Main():
    #Task_1()
    Task_2()
    print('\n\n\n')
    Task_3()

# ***************************************************************************

if __name__ == "__main__": Main()