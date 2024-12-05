from Hatoslotto import Lotto

def file_beolvas(filenev:str=""):
    huzas_lista=[]
    fajlom = open("huzasok.txt", "r", encoding='UTF-8')
    elso_sor = fajlom.readline()
    sorok_lista = fajlom.readlines()
     
    for i in range(0, len(sorok_lista), 1):
            sor = sorok_lista[i].strip()
            sor_lista=sor.split("@")
            huzas = Lotto(sor_lista[0],sor_lista[1],sor_lista[2],sor_lista[3])
            huzas_lista.append(huzas)
    fajlom.close()
    return huzas_lista

def sor_kiiras(huzas_lista):
    print("III/A, B:")
    print(f"A húzások száma: {len(huzas_lista)}\n")

def huzasok_atlaga(huzas_lista):
    szamok:float = 0
    db:float = 0
    for i in range(0, len(huzas_lista), 1):
        if(huzas_lista[i].het == 42):
            szamok += huzas_lista[i].szam
            db += 1
    osszes_huzas_atlaga:float = szamok / db
    print("III/C:")
    print(f"A 42. héten húzott számok átlaga: {osszes_huzas_atlaga:.2f}\n")

def legnagyobb_huzas(huzas_lista):
    legnagyobb_szam:int=0
    for i in range(0, len(huzas_lista), 1):
        if (huzas_lista[i].szam > legnagyobb_szam):
            legnagyobb_szam = huzas_lista[i].szam
            ev = huzas_lista[i].ev
            het = huzas_lista[i].het
            huzas = huzas_lista[i].huzas
    return legnagyobb_szam, ev, het, huzas

def legnagyobb_kiiras(legnagyobb_szam, ev, het, huzas):
    print("III/D:")
    print(f"Az első legnagyobb kihúzott szám értéke: {legnagyobb_szam} , {ev}-ben, a {het}. héten húzták ki, ez volt a {huzas}. húzás.")