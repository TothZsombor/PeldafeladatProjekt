#Számológép

def main():
    szam1 = szambekeres('Adja meg az első számot: ')
    szam2 = szambekeres('\nAdja meg a második számot: ')
    muvelet_valasz = muvelet_valasztas()    #2* Kiegészítés
    muvelet(muvelet_valasz, szam1, szam2)
    megfordit(szam1, szam2)



def szambekeres(kiiras: str) -> int:    #Kiegészítés
    szam = 0
    try:
        szam = int(input(kiiras))
    except:
        szam: int = szambekeres('Kérem számot adjon meg: ') #Kiegészítés
    return szam

def muvelet_valasztas():
    print('\nVálasszon műveletet: ')    #Kiegészítés
    print('\t1..Összeadás')
    print('\t2..Kivonás')
    print('\t3..Szorzás')
    print('\t4..Osztás')
    print('\t0..Kilépés')

    v = 100     #Javítás
    while v != '0' and v != '1' and v != '2' and v != '3' and v != '4':
        v = input('Választás: ')
    return v

def muvelet(mv: str, szam1: int, szam2: int):
    match mv:
        case '0':
            exit()
        case '1':
            print(f'\nEredmény: {szam1 + szam2}')
        case '2':
            print(f'\nEredmény: {szam1 - szam2}')
        case '3':       # 2* Kiegészítés
            print(f'\nEredmény: {szam1 * szam2}')
        case '4':
            print(f'\nEredmény: {szam1 / szam2}')

def megfordit(szam1: int, szam2: int):      #Teljes függvény
    v = input("\nSzeretné megfordítani a számokat? Igen/Nem: ")
    if v == "Igen":
        mv = muvelet_valasztas()
        muvelet(mv, szam2, szam1)

main()