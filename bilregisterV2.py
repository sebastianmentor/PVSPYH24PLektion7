bilregister = {"ABC123": 
                {   "märke":"BMW",
                    "färg":"Blå",
                    "årsmodell":"2020",
                    "pris":"200000"
                    }
            }
# registreringsnummer -> ABC123
# bil -> {'märke':märke, 'färg':färg, 'årsmodell':årsmodell, 'pris':pris}
# bilregister -> {registreringsnummer : bil}

def lägga_till_ny_bil(regnr):
    märke = input("Ange märke: ")
    färg = input("Ange färg: ")
    årsmodell = input("Ange årsmodell: ")
    pris = input("Ange nuvarande pris: ")

    bil = dict(
        märke=märke, 
        färg=färg, 
        årsmodell=årsmodell, 
        pris=pris
        )

    bilregister[regnr] = bil

def kolla_upp_bil(regnr):
    bil = bilregister[regnr]
    print(f"{regnr}:")
    for key,val in bil.items():
        print(f"\t{key} : {val}")
    print()

def ändra_färg_eller_pris(regnr,ändring):
    nytt_värde = input(f"Ange nytt värde: ")
    bilregister[regnr][ändring] = nytt_värde

def ändra_biluppgifter(regnr):
    print("1. Färg")
    print("2. Pris")
    ändring = input("Vad önskas ändras?")

    if  ändring == "1":
        ändra_färg_eller_pris(regnr, "färg")

    elif ändring == "2":
        ändra_färg_eller_pris(regnr, "pris")

    else:
        print("Fel input! Återgår till menyn!")



def kontrollera_om_regnr_finns(regnr):
    if regnr in bilregister:
        return True
    else:
        return False

def hantera_bil(val):
    regnummer = input("Skriv in regnummer: ")
    finns_bil = kontrollera_om_regnr_finns(regnummer)

    if val == "1":
        if finns_bil:
            print('Bilen finns redan!')
        else:
            lägga_till_ny_bil(regnummer)

    elif val == "2" and finns_bil:
        kolla_upp_bil(regnummer)

    elif val == "3" and finns_bil:
        ändra_biluppgifter(regnummer)
    
    else:
        print('Bilen finns inte i registret!!!')

def main():
    print("Välkommen till Lasses Bilkoll!")

    while True:
        print("1. Lägg till ny bil")
        print("2. Kolla upp bil")
        print("3. Ändra biluppgifter")
        print("4. Skriv ut bilregister")
        print("5. Avsluta")

        val = input("Vänligen gör ett val: ")

        if val in ['1','2','3']:
            hantera_bil(val)

        elif val == "4":
            for regnr, bil in bilregister.items():
                print(f"{regnr} : {bil}")

        elif val == "5":
            break

        else:
            print("Ogiltligt val!")


if __name__ == "__main__":
    main()