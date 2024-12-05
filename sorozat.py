import random

def randomszamok():
    print("II/A, B, C:\n")
    szam_lista=[]
    i:int = 0
    while (i <= 7):
        szam:int = random.randint(-100,859)
        if i < 7:
            print(f"{szam}", end=";")
            szam_lista.append(szam)
            i += 1
        elif i == 7:
            print(f"{szam}")
            szam_lista.append(szam)
            i += 1
    return szam_lista

def tizzel_oszthatoak_szama(szam_lista):
    i:int = 0
    tizzel_oszthato_szamlalo:int = 0
    for i in range(0, len(szam_lista), 1):
        if szam_lista[i] % 10 == 0:
            tizzel_oszthato_szamlalo += 1
    return tizzel_oszthato_szamlalo

def konzol_ir(tizzel_oszthato_szamlalo):
    print("II/D, E:\n")
    print(f"Tízzel osztható számok száma: {tizzel_oszthato_szamlalo}.")

def fajlba_ir(tizzel_oszthato_szamlalo):
    fajlom = open("vegeredmeny.txt", "w", encoding="UTF-8")
    fajlom.write(f"Tízzel osztható számok száma: {tizzel_oszthato_szamlalo}.")
    fajlom.close
