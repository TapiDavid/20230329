import os

class Tanulo:
    def __init__(self,azonosito):
        
        self.azonosito = str(azonosito)
        self.vez_nev = input("A tanuló vezetékneve: ")
        self.ker_nev = input("A tanuló keresztneve: ")
        self.szul_ev = input("A tanuló születési éve: ")
        self.kor = str(2023-int(self.szul_ev))
        self.atlag = input("A tanuló tanulmányi átlaga: ")

megnyitas_mod = ""

if os.path.exists("Tanulo_adatbazis.txt"):
    megnyitas_mod = "a+"
else:
    megnyitas_mod = "w"



with open("Tanulo_adatbazis.txt",megnyitas_mod,encoding="UTF-8") as celfajl,\
    open("Tanulo_adatbazis.txt","r",encoding="UTF-8") as forrasfajl:

    if megnyitas_mod == "w":
        print("Azonosító;Vezetéknév;Keresztnév;Születési év;Kor;Átlag",file=celfajl)
        fajl_hossza = 1

    if megnyitas_mod == "a+":
        fajl_hossza = 0
    
        for j in forrasfajl:
            fajl_hossza += 1

    megegy_tanulo = "i"

    while megegy_tanulo == "i":

        tanulo_sor = ""

        tanulo_objektum = Tanulo(fajl_hossza)
        tanulo_sor += tanulo_objektum.azonosito + "," + tanulo_objektum.vez_nev + "," + tanulo_objektum.ker_nev + "," + tanulo_objektum.szul_ev + "," + tanulo_objektum.kor + "," + tanulo_objektum.atlag

        print(tanulo_sor,file=celfajl)

        fajl_hossza += 1

        print("")
        megegy_tanulo = input("Szeretnél mégegy tanulót hozzáadni? (i/n) ")
        while megegy_tanulo != "i" and megegy_tanulo != "n":
           megegy_tanulo = input("Igen vagy nem? (i/n) ")
        print("")
