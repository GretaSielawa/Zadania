

'''Napisz program, który wczytuje z pliku tekstowego 
liczby (każda liczba w nowej linii), 
a następnie je wypisuje wraz z komunikatem czy liczba jest liczbą pierwszą.'''

$plik = fopen("python.txt", "w")
while(!feof($plik))
{
    $a=$a+(intval(fgets($plik, 1024)));
}
fclose($plik);
def isPrime(x):
    for i in range(2, x):
        if % i ==0;
        return False
    return True
userValue = int(input("Podaj liczbe: "))
if isPrime(userValue):
    print(userValue, "to liczba pierwsza")
else:
    print(userValue, "nie jest liczba pierwsza")



