#1/. feladat
from feladat3_osztaly import Versenyzo

versenyzok: list[Versenyzo] = []

#/2. feladat    -> 5 pont: 1 lista létrehozás és fájl megnyitás/bezárás, 1 első sor átugrás és beolvasás, 1 vessző/pont, 2 monogram
f = open("megoldas_python/mukorcsolya.csv", "r", encoding="UTF-8")
f.readline()
for sor in f:
    versenyzok.append(Versenyzo(sor))
f.close()

#3. feladat     -> 1 pont
print(f"3. feladat: Összesen {len(versenyzok)} versenyző jutott a szabad programba.")

#4. feladat     -> 3 pont: 2 pont max keresés, 1 pont helyes kiírás
#Legnagyobb pontszám szabad programban
maxV: Versenyzo = versenyzok[0]
for v in versenyzok[1:]:
    if maxV.szabadp < v.szabadp:
        maxV = v

print("\n4. feladat: A legtöbb pontszámot elért versenyző a Szabadprogramban:")
print(f"\tVersenyző: {maxV.nev}")
print(f"\tNemzet: {maxV.nemzet}")
print(f"\tSzabadprogram pontszám: {maxV.szabadp}")

#5. feladat     -> 4 pont: 1 pont helyes bekérés, 2 pont helyes függvények, 1 pont helyes kiírás
#Egy nemzet által elért összes pontszám
#Elírt nemzetet nem kell ellenőrízni
print("\n5. feladat: Melyik nemzet összpontszámát szeretné tudni?")
kert_nemzet = input("\tA nemzet hárombetűs kódja: ")
ossz: float = 0
for v in versenyzok:
    if v.nemzet == kert_nemzet:
        ossz += v.osszp
print(f"\tA(z) {kert_nemzet} nemzet {ossz} pontszámot ért el.")

#6. feladat     -> 
#5 pont: 1 pont a bevezető címért és helyes fájlnév, 1 pont a helyes formátumért(fájlnév, sor szerkezete), 1 pont a max keresésért, 1 pont a helyes értékekért(függvény használatával),  1 pont a háromszori megkeresésre és top kiszedése a listából
#Írd ki a top 3 helyezést fájlba
f = open("dobogo.csv", "w", encoding="UTF-8")
f.write("Nev;Nemzet;Helyezes;Osszesites;RovidProgram;SzabadProgram\n")

for i in range(0,3):
    maxVersenyzo: Versenyzo = versenyzok[0]
    for v in versenyzok[1:]:
        if maxVersenyzo.osszp < v.osszp:
            maxVersenyzo = v
    versenyzok.remove(maxVersenyzo)
    f.write(f"{maxVersenyzo.nev};{maxVersenyzo.nemzet};{i+1};{maxVersenyzo.osszp};{maxVersenyzo.rovidp};{maxVersenyzo.szabadp}\n")

