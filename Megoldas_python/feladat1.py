'''
1eur = 390,82 Ft ||| 1 forint = 0,0026 Eur
1font = 457,35 Ft ||| 1 forint = 0,0022 Font
1dollar = 364,59 Ft ||| 1 forint = 0,0027 Dollar
'''

#Feltételezzük hogy a felhasználó helyes adatot ad be
bekert_adat = int(input('Hány forintot szeretne átváltani más pénznemmé? '))

#Átváltás
print(f'{bekert_adat} Ft =')
print(f'\t{bekert_adat * 0.0026:.2f} Euro')
print(f'\t{bekert_adat * 0.0022:.2f} Font')
print(f'\t{bekert_adat * 0.0027:.2f} Dollar')

#Árfolyam megadva,nincs kezdőfájl