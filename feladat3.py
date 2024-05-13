#1. feladat
from feladat3_osztaly import Versenyzo

versenyzok: list[Versenyzo] = []

#2. feladat
f = open("versenyzok.csv", "r", encoding="UTF-8")
f.readline()
for sor in f:
    versenyzok.append(Versenyzo(sor))
f.close()

#3. feladat
print(f"3. feladat: Összesen {len(versenyzok)} versenyző jutott a szabad programba.")

#4. feladat
#Legnagyobb pontszám szabad programban
maxV: Versenyzo = versenyzok[0]
for v in versenyzok[1:]:
    if maxV.szabadp < v.szabadp:
        maxV = v

print("\n4. feladat: A legtöbb pontszámot elért versenyző a Szabadprogramban:")
print(f"\tVersenyző: {maxV.nev}")
print(f"\tNemzet: {maxV.nemzet}")
print(f"\tSzabadprogram pontszám: {maxV.szabadp}")

#5. feladat
#Egy nemzet által elért összes pontszám
#Elírt nemzetet nem kell ellenőrízni
kert_nemzet = input("\n5. feladat: Melyik nemzet összpontszámát szeretné tudni? ")
ossz: float = 0
for v in versenyzok:
    if v.nemzet == kert_nemzet:
        ossz += v.osszp
print(f"\tA(z) {kert_nemzet} nemzet {ossz} pontszámot ért el.")

#6. feladat
#Írd ki a top 3 helyezést fájlba
f = open("top3.csv", "w", encoding="UTF-8")
f.write("Nev;Nemzet;Helyezes;Osszesites;RovidProgram;SzabadProgram\n")

for i in range(0,3):
    maxVersenyzo: Versenyzo = versenyzok[0]
    for v in versenyzok[1:]:
        if maxVersenyzo.osszp < v.osszp:
            maxVersenyzo = v
    versenyzok.remove(maxVersenyzo)
    f.write(f"{maxVersenyzo.nev};{maxVersenyzo.nemzet};{i+1};{maxVersenyzo.osszp};{maxVersenyzo.rovidp};{maxVersenyzo.szabadp}\n")

