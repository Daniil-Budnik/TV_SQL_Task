import Telecast as TL
import Client as CL
import Ad as AD

from DataBaseMain import DataBaseMain

import json as JS

class Accounting(DataBaseMain):

    def read(self, file_name):

        with open(file_name) as Files: data = JS.load(Files)

        for item in data["clients"]:
            client = CL.Client(item["id"], item["companyName"], item["bankData"], item["phone"], item["contact"])
            self._DataBaseMain__clients.append(client)

        for item in data["telecasts"]:
            telecast = TL.Telecast(item["id"], item["name"], item["rating"], item["price"])
            self._DataBaseMain__telecasts.append(telecast)

        for item in data["ads"]:
            ad = AD.Ad(item["id"], self._DataBaseMain__telecasts.getByID(item["telecast"]), 
                       self._DataBaseMain__clients.getByID(item["client"]),item["date"], item["time"])
            self._DataBaseMain__ads.append(ad)

    # ***************************************************************************

    def write(self, file_name):

      if file_name.endswith(".json"):

          clients = []
          for item in self._DataBaseMain__clients:
              client = {
                  "id": item.getID(),
                  "companyName": item.getCompanyName(),
                  "bankData": item.getBankData(),
                  "phone": item.getPhone(),
                  "contact": item.getContact()
              }
              clients.append(client)

          telecasts = []
          for item in self._DataBaseMain__telecasts:
              telecast = {
                  "id": item.getID(),                  
                  "name": item.getName(),              
                  "rating": item.getRating(),          
                  "price": item.getPrice()
              }
              telecasts.append(telecast)

          ads = []
          for item in self._DataBaseMain__ads:
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