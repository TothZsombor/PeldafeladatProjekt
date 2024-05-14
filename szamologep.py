#Számológép

def main():
    szam1 = szambekeres('Adja meg az első számot: ')
    szam2 = szambekeres('\nAdja meg a második számot: ')
    

def szambekeres() -> int:
    szam = 0
    try:
        szam = int(input(kiiras))
    except:
        szam: int = szambekeres('')
    return szam

      

main()