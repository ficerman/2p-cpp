duotrigA = ["A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N",
"O",
"P",
"Q",
"R",
"S",
"T",
"U",
"V"]

def sept(x):
    y=str()
    while (int(x)!=0):
        y = str(int(int(x)%7)) + y
        x = int(x / 7)
    return y

def duotrig(x):
    y=str()
    while (int(x)!=0):
        if(int(int(x)%32) > 9):
            y = duotrigA[int(int(x)%32) - 10] + y
        else:
            y = str(int(int(x)%32)) + y
        x = int(x / 32)
    return y

def drukuj(liczba):
    print("system dziesietny: " + str(liczba))
    print("system binarny: " + bin(liczba))
    print("system szesnastkowy: " + hex(liczba))
    print("system oktetowy: " + oct(liczba))
    print("system siodemkowy: " + sept(liczba))
    print("system trzydziestodwojkowy: " + duotrig(liczba))
    print()

liczba = int(input("Wprowadz liczbe w systemie dziesietnym:"))
drukuj(liczba)
liczba = int(input("Wprowadz liczbe w systemie binarnym:"), 2)
drukuj(liczba)
