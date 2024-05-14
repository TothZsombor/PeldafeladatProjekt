#Számológép

def main():
    szam1 = szambekeres('Adja meg az első számot: ')
    szam2 = szambekeres('\nAdja meg a második számot: ')
    muvelet_valasz = muvelet_valasztas()
    muvelet(szam1, szam2)



def szambekeres() -> int:
    szam = 0
    try:
        szam = int(input(kiiras))
    except:
        szam: int = szambekeres('')
    return szam

def muvelet_valasztas():


    v = '1'
    while v != '1' and v != '2' and v != '3' and v != '4':
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
        case '3':
            print(f'\nEredmény: {szam1 * szam2}')
        case '4':
            print(f'\nEredmény: {szam1 / szam2}')



main()