

def bekeres():
    ertekeles_bekeres:int=456
    print("I/A, B:\n")
    nap_bekeres = str(input("Hét napja: "))
    tanora_bekeres = str(input("Óra neve: "))
    while not (ertekeles_bekeres >=0 and ertekeles_bekeres <=5):
        ertekeles_bekeres:int = int(input("Értékelés (0-5): "))
        if (ertekeles_bekeres < 0):
            print("Az értékelés nem lehet negatív!")
        elif (ertekeles_bekeres > 5):
            print("5 pont feletti értékelés nem elfogadható!")
        else:
            print("Köszönjük az értékelést!")
    return ertekeles_bekeres, nap_bekeres, tanora_bekeres

def kiiras(ertekeles_bekeres, nap_bekeres, tanora_bekeres):
    print("I/C:\n")
    print(f"Összefoglaló: '{nap_bekeres}','{tanora_bekeres}',{ertekeles_bekeres} érték")