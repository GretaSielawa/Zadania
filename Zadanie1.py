'''Napisz program, który pobierze od użytkownika rok urodzenia, następnie obliczy 
i wypisze wiek oraz wypisze informację, czy użytkownik jest pełnoletni.'''  

import time

birthYear = int(input("Podaj swoj rok urodzenia: "))
age = 2021 - birthYear
if birthYear >= 2022:
    print("Bledny rok urodzenia!")
else:
    print("Twoj wiek to ", age, "lat!")
    if birthYear >= 18:
        print("Jestes pelnoletni!")
time.sleep(60)
