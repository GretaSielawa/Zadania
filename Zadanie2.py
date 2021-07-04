import time
'''Napisz program, który wyświetli w nowych liniach kolejny liczby całkowite od 1 do 100
oraz przy liczbach podzielnych przez 3 wypisze "GOOD", 
przy liczbach podzielnych przez 5 "BETTER", a przy podzielnych przez 3 i przez 5 "BEST".
'''

value = 0;
for value in range(1, 100+1):
    if value % 3 == 0:
        print(value, "GOOD")
    if value % 5 == 0:
        print(value, "BETTER")
    if value % 3 and value % 5:
        print(value, "BEST")
    time(seconds(60))



