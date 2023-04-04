class Tanulo:
    def __init__(self,sor):
        sor = sor.split(",")

        self.azonosito = sor[0]
        self.vez_nev = sor[1]
        self.ker_nev = sor[2]
        self.szul_ev = sor[3]
        self.kor = sor[4]
        self.atlag = sor[5]

with open("Tanulo_adatbazis.txt","r",encoding="UTF-8") as forrasfajl:

    Osztaly = []

    fejlec = True

    for i in forrasfajl:
        if fejlec == True:
            fejlec = False
        else:
            Osztaly.append(Tanulo(i))


letszam = 0
tizennegynel_idosebb = 0
van_e_varga = False
osztaly_atlag = 0

legjobb_atlag_tanulo = ""
legjobb_atlag = 0

legrosszabb_atlag_tanulo = ""
legrosszabb_atlag = 0

for j in Osztaly:

    letszam += 1

    osztaly_atlag += int(j.kor)

    if int(j.kor) > 14:
        tizennegynel_idosebb += 1

    if j.vez_nev == "Varga":
        van_e_varga = True

osztaly_atlag = osztaly_atlag/letszam

legjobb_atlag_tanulo = Osztaly[0].vez_nev + " " + Osztaly[0].ker_nev
legjobb_atlag = Osztaly[0].atlag

legrosszabb_atlag_tanulo = Osztaly[0].vez_nev + " " + Osztaly[0].ker_nev
legrosszabb_atlag = Osztaly[0].atlag

for k in Osztaly:
    if float(k.atlag) > float(legjobb_atlag):
        legjobb_atlag = k.atlag
        legjobb_atlag_tanulo = k.vez_nev + " " + k.ker_nev
    elif float(k.atlag) == float(legjobb_atlag):
        legjobb_atlag_tanulo += ", " + k.vez_nev + " " + k.ker_nev


    if float(k.atlag) < float(legrosszabb_atlag):
        legrosszabb_atlag = k.atlag
        legrosszabb_atlag_tanulo = k.vez_nev + " " + k.ker_nev
    elif float(k.atlag) == float(legrosszabb_atlag):
        legrosszabb_atlag_tanulo += ", " + k.vez_nev + " " + k.ker_nev

print("A csoport létszáma",str(letszam)+".")
print("A 14 évesnél idősebb tanulók száma",str(tizennegynel_idosebb)+".")
print("Az osztályátlag","%.2f" % float(osztaly_atlag)+".")
if van_e_varga == True:
    print("Van 'Varga' vezetéknevű tanuló az osztályban.")
else:
    print("Nincs 'Varga' vezetéknevű tanuló az osztályban.")
print("A legjobb átlaga",legjobb_atlag_tanulo,"tanuló(k)nak van.")
print("A legrosszabb átlaga",legrosszabb_atlag_tanulo,"tanuló(k)nak van.")
