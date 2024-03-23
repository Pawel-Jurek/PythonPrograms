#zadanie dzielniki
num = int(input("Please choose a number to divide: "))
for i in range(1,num):
    if num % i == 0:
        print(i)

#zadanie dodawanie wspólnych elementów
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    if i in b and i not in c: 
        c.append(i)
print(c)

#zadanie palindrom
def czypalindrom():
    wyraz = input("Podaj wyraz: ")
    return wyraz==wyraz[::-1] 

#zadania lista jedna linijka nieparzyste
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even=[i for i in a if i % 2 == 1]

#zadania cisaki
def sprawdzenie_zgodnosci(gracz1, gracz2):
     return gracz1 in Figura and gracz2 in Figura

def ruch(gracz1, gracz2):
    match gracz1.split():
        case["Nozyce"]:
            print("Wygral gracz 2") if gracz2 == "Kamien" else print("Wygral gracz 1")               
        case["Kamien"]:
            print("Wygral gracz 2") if gracz2 == "Papier" else print("Wygral gracz 1")
        case["Papier"]:
            print("Wygral gracz 2") if gracz2 == "Nozyce" else print("Wygral gracz 1")
    
Figura = ("Papier", "Kamien", "Nozyce")
decyzja = "tak"
while decyzja != "exit":
    gracz1 = input("Ruch gracza 1: ")
    gracz2 = input("Ruch gracza 2: ")
    ruch(gracz1, gracz2) if(gracz1!=gracz2) else print("Remis") if sprawdzenie_zgodnosci(gracz1, gracz2) else print("Bledne dane")
    decyzja = input("Wpisz cokolwiek zeby grac dalej lub exit, zeby zakonczyc: ")        

#zadanie guess a number

import random
poprawna = random.randint(1,9)
proba=1
odp = int(input("Zgadnij liczbe pomiedzy 1 i 9: "))
while odp != poprawna:
    print("za duzo") if odp > poprawna else print("za malo")
    odp = int(input("Zgadnij liczbe pomiedzy 1 i 9: "))
    proba+=1

print("GRATULACJE, poprawna liczba to: " + str(poprawna) + " zgadles w probie: " + str(proba))

#zadanie montowanie listy z dwóch list, te same liczby
import random
a = random.sample(range(15), 7)
b = random.sample(range(15), 9)
c = [i for i in a if i in b]
print("a -> ", end="")
print(a)
print("b -> ", end="")
print(b)
print("c -> ", end="")
print(c)

#zadanie czy libcza jest pierwsza
def get_integer():
    return int(input("Podaj liczbe: "))
    
def IsPrimaly(liczba):
    nowa_liczba=liczba-1
    for i in range(2,nowa_liczba):
        if liczba % i == 0:
            return False
    return True
            
def ShowAnswer(answer):
    print("Jest pierwsza") if answer else print("Nie jest pierwsza")
    
ShowAnswer(IsPrimaly(get_integer()))

#zadanie pierwszy i ostatni element listy
a = [5, 10, 15, 20, 25]
c = [a[0],a[len(a)-1]]
print(c)

#zadanie fibonacci //zadanie13
def fib(n):
    if n < 3: return 1
    return fib(n-1)+fib(n-2)
    
   
#zadanie 14 set
a = [1,2,3,4,3,2,1,2,3,2]
b = set(a)

#zadanie 15 odworcona kolenjosc wyrazow
def get_text():
    return input("Podaj tekst: ")

def reverse_text(tekst):
    tekst = tekst.split()
    return " ".join(tekst[::-1])
    
print(reverse_text(get_text()))

#zadanie 16 hasło generator
import random
import string

def losuj_znak():
    alfabet = string.ascii_uppercase + string.ascii_lowercase
    return random.choice(alfabet)

def losuj_liczbe():
    return random.randint(0,9)
    
dlugosc = int(input("Podaj dlugosc hasla: "))
haslo = ""
for i in range(0,dlugosc):
    wybor = random.randint(0,1)
    haslo += (losuj_znak() if wybor == 0 else str(losuj_liczbe()))
print(haslo)

#zadanie 17 i 19 do zrobienia!!!

#zadanie 18 krowy i byki

import random
def losuj_liczbe():
    return random.randint(0,9)
def napraw_user_liczbe(liczba):
    return "0" * (4 - len(liczba)) + liczba
liczba = ""
for i in range (0,4):
    liczba += str(losuj_liczbe())
print(liczba)
user_liczba = str(input("podaj liczbe: "))
proby = 1
while liczba != user_liczba:
    if len(user_liczba) < 4:
        user_liczba = napraw_user_liczbe(user_liczba)
    krowy = 0
    byki = 0
    for i in range(0,4):
        if liczba[i] == user_liczba[i]:
            krowy+=1 
        if user_liczba[i] in liczba: 
            byki+=1
    if krowy == 4:
        break
    byki -= krowy
    print("krowy: " + str(krowy))
    print("byki: " + str(byki))
    user_liczba = str(input("podaj liczbe: "))
    proby+=1
print("zgadles w probie nr: " + str(proby))            

#zadanie 20 czy liczba w liscie
def find_element(szukana, lista, poczatek, koniec):
        print(str(poczatek) + " " + str(koniec))
        if poczatek + 1 == koniec and lista[poczatek] != szukana:
            return False
        nowa_granica = (koniec + poczatek) / 2
        liczba = lista[nowa_granica]
        return True if liczba == szukana else find_element(szukana, lista, nowa_granica, koniec) if liczba < szukana else find_element(szukana, lista, poczatek, nowa_granica)

#zadanie 21 zapis do pliku
def zapis(nazwa, tekst):
    with open(nazwa, 'w') as otwarty_plik:
        otwarty_plik.write(tekst)
        
#zadanie 22 czytanie pliku i słowniki -> ile każdego z imion w pliku
def read_file(file_name):
    with open(file_name, "r") as opened_file:
        return opened_file.read()

def count_names(names):
    names = names.split()
    CountedNames = {} 
    for i in names:
        CountedNames[i]+=1
    return CountedNames
    
def show_data(CountedNames):
    for i in CountedNames:
        print(i)

#zadanie 22 czytanie z pliku + słowniki
def read_file(file_name):
    with open(file_name, 'r') as open_file:
        return open_file.read()
        
def count_names(names):
    names = names.split()
    counted_names = {}
    for i in names:
        if i in counted_names:
            counted_names[i] += 1
        else:
            counted_names[i] = 1          
    return counted_names

def show_stats(stats):
    for i in stats.items():
        print(i)
        
#zadanie 22 trudniejsza wersja
def count_categories(text):
    text = text.split()
    counted_categories = {}
    for i in text:
        i = i[3:i.rfind('/')]
        if i in counted_categories:
            counted_categories[i] += 1
        else:
            counted_categories[i] = 1          
    return counted_categories
    
#zadanie 23 odczyt i zwrocenie liczb ktore wystepuja w obu plikach

def read_file(file_name):
    with open(file_name, 'r') as open_file:
        return open_file.read()

def run(file_name, file2_name):
    a = read_file(file_name).split()
    b = read_file(file2_name).split()
    print (get_shared(a,b))

def get_shared(b, c):
    shared = set()
    shared.update(b)
    shared.update(c)
    return [i for i in shared if i in b and i in c]

#zadanie 24 plansza tic tac toe

def draw_game_board(size):
    for i in range(0,size*2+1):
        if i % 2 == 0:
            for j in range(0,size):
                print(" ---", end="")
        else: 
            for j in range(0,size+1):
                print("|   ", end="")
        print("")

draw_game_board(3)

#zadanie 25 guess a number by comp
def guess_a_number():
    global proba
    proba = 0
    szukana = int(input("Podaj liczbe do zgadniecia: "))
    dolna = int(input("Podaj dolna granice: "))
    gorna = int(input("Podaj gorna granice: "))
    znaleziona = find_element(szukana, dolna, gorna)
    print("Znaleniona liczba: " + str(znaleziona))
    print("W probie: " + str(proba))
    
def find_element(szukana, poczatek, koniec):
    global proba 
    proba += 1
    print(str(poczatek) + " " + str(koniec))
    liczba = int((koniec + poczatek) / 2)
    if poczatek + 1 == koniec and liczba != szukana:
        return -1
    return liczba if liczba == szukana else find_element(szukana, liczba, koniec) if liczba < szukana else find_element(szukana, poczatek, liczba)
    
#zadanie 26 check who win tic tac toe
game = [[0,0,2],
        [1,1,0],
        [1,0,2]]

def Check_rows(game):
    for i in range(0,len(game)):
        if all(game[i]) == 1: 
            return 1
        elif all(game[i]) == 2:
            return 2
    return 0        
    
def Check_diagonals(game):
    diagonal1 = []
    diagonal2 = []
    size = len(game)
    for i in range(0, size):
        diagonal1.append(int(game[i][i]))
        diagonal2.append(int(game[i][size-i-1]))
    if all(number == 1 for number in diagonal1) or all(number == 1 for number in diagonal2): 
        return 1
    elif all(number == 2 for number in diagonal1) or all(number == 2 for number in diagonal2): 
        return 2
    else:
        return 0
        
def CheckWhoWon(game):
    if Check_diagonals(game) != 0:
        return Check_diagonals(game)
    elif Check_rows(game) != 0:
        return Check_rows(game)
    else:
        import numpy as np
        arr = np.array(game)
        return Check_rows(arr.transpose())
            

#zadanie 27 wprowadzanie danych do gry tic tac toe

def player_move(player):
    global game
    while(True):
        RowCol = str(input("Kolej gracza: " + str(player) +" Podaj wiersz i kolumne oddzielone spacjom: "))
        RowCol = RowCol.split()
        Row = int(RowCol[0])
        Col = int(RowCol[1])
        if game[Row][Col] == '0':
            game[Row][Col] = ("X" if player == 1 else "O")
            break
        else:
            print("Ta komorka jest juz zajeta lub nie istnieje!!!")
            break
            
def draw_game_board(size):
    global game
    for k in range(0,size):
        print("  k" + str(k), end="  ")
    print("")
    for i in range(0,size*2+1):
        if i % 2 == 0:            
            for j in range(0,size):
                print(" ---", end="  ")
        else: 
            for j in range(0,size):
                print("|", end=" ")
                print(game[int(i/2)][j] + " | ", end="")
            print(" w"+str(int(i/2)), end="")
        print("")

def gameplay():
    global game
    game = [['0','0','0'],['0','0','0'],['0','0','0']]
    i = 0
    result = CheckWhoWon(game)
    draw_game_board(len(game))
    while result == 0 and i < 9:
        if i % 2 == 0:
            player_move(1)
        else:
            player_move(2)
        draw_game_board(len(game))
        i += 1
        result = CheckWhoWon(game)
    match result:
        case 0: 
            print("Remis")
        case 1: 
            print("Wygral gracz 1")
        case 2: 
            print("Wygral gracz 2")
        case other:
            print("Nie znaleziono")
    
        
def Check_rows(game):
    for i in range(0,len(game)):
        if all(game[i]) == "X": 
            return 1
        elif all(game[i]) == "O":
            return 2
    return 0        
    
def Check_diagonals(game):
    diagonal1 = []
    diagonal2 = []
    size = len(game)
    for i in range(0, size):
        diagonal1.append(game[i][i])
        diagonal2.append(game[i][size-i-1])
    if all(char == "X" for char in diagonal1) or all(char == "X" for char in diagonal2): 
        return 1
    elif all(char == "O" for char in diagonal1) or all(char == "O" for char in diagonal2): 
        return 2
    else:
        return 0
        
def CheckWhoWon(game):
    if Check_diagonals(game) != 0:
        return Check_diagonals(game)
    elif Check_rows(game) != 0:
        return Check_rows(game)
    else:
        import numpy as np
        arr = np.array(game)
        return Check_rows(arr.transpose())
        
#zadanie 28 max of three
lista = [input("Podaj liczbe: ") for i in range (0,3)]
print (max(lista))

#zadanie 29 picking the word to hangman game
def open_file(filename):
    whole = []
    with open(filename, 'r') as f:
        line = f.readline().strip()
        while line:
            line = f.readline().strip()
            whole.append(line)
    return whole  
  
import random

def random_word(words):
    return words[random.randint(0,len(words)-1)]
    

def gameplay():
    word = random_word(open_file("sowpods.txt"))
    result = "_ " * len(word)
    print("Witaj w grze wisielec :)\n")
    wrong_anws = 0
    while result.replace(" ","") != word and wrong_anws < 6:
        print(result + "\n")
        letter = input("Zgadnij litere: ")
        letter = letter.upper()
        if letter in word:
            find_all = lambda c,s: [x for x in range(c.find(s), len(c)) if c[x] == s]
            pos = find_all(word, letter)
            for i in pos:
                lista = list(result)
                lista[2 * i] = letter
                result = "".join(lista)                
        else:
            wrong_anws += 1
            print("Zla odpowiedz " + str(wrong_anws) + "/6")
        print("\n")
    print("Przegrales/as :(\nPoprawne rozwiazanie: "+ word) if wrong_anws == 6 else print(result + "\nGratulacje!! Wygrales/as!")
    
#generator danych do zadania
def zapis(nazwa, tekst):
    with open(nazwa, 'w') as otwarty_plik:
        otwarty_plik.write(tekst)
        
imiona = ["Adam ", "Marcin ", "Pawel ", "Szymon ", "Kamil ", "Tomasz ", "Andrzej", "Krzysztof", "Albert", "Ernest"]
nazwiska = ["Konieczy ", "Pawelczuk ", "Lubina ", "Czajka ", "Witkowski ", "Siminski ", "Kaczor ", "Grabowski ", "Szyjer ", "Kapusta ", "Placek "]
tekst = ""
def generate_date():
    miesiac = random.randint(1,12)
    if miesiac < 10:
        miesiac = str(miesiac)
        miesiac = miesiac.replace(miesiac[0],"0"+ miesiac[0])
    return str(random.randint(1,28))+"/"+ str(miesiac) +"/"+str(random.randint(1970,2000))
for i in range(0, 15):
    tekst = tekst + str(imiona[random.randint(0,6)]) + str(nazwiska[random.randint(0,10)]) + generate_date() + "\n"

zapis("urodziny.txt", tekst)

#zadanie 33 slownik urodzin

def open_file(filename):
    urodziny = {}
    with open(filename, 'r') as f:
        line = "a"
        while line:
            line = f.readline().strip()
            podzielona = line.split()
            if len(podzielona) > 0:
                urodziny[str(podzielona[0]+ " "+ podzielona[1])] = podzielona[2]
    return urodziny  
 
def findingdate():
    urodziny = open_file("urodziny.txt")
    for key, value in urodziny.items() :
        print (key)
    wybor = input("\nPodaj imie i nazwisko osoby, ktorej date urodzin chcesz poznac: ")
    print(urodziny[wybor]) if wybor in urodziny else print("Brak takiej osoby")
    
#zadanie 34 słownik urodzin z plikiem json
import json

def zapisjson(nazwa, ludzie):
    with open(nazwa + ".json", "w") as f:
        json.dump(ludzie, f)

def generate_dict(): 
    imiona = ["Adam", "Marcin", "Pawel", "Szymon", "Kamil", "Tomasz", "Andrzej", "Krzysztof", "Albert", "Ernest", "Lech"]
    nazwiska = ["Konieczny", "Pawelczuk", "Lubina", "Czajka", "Witkowski", "Siminski", "Kaczor", "Grabowski", "Szyjer", "Kapusta", "Placek"]
    people = {}
    for i in range(0, len(imiona)):  
        for j in range(0,len(nazwiska)):           
            people[imiona[i]+ " "+ nazwiska[j]] = generate_date()
    return people
    
def generate_date():
    miesiac = random.randint(1,12)
    if miesiac < 10:
        miesiac = str(miesiac)
        miesiac = miesiac.replace(miesiac[0],"0"+ miesiac[0])
    return str(random.randint(1,28))+"/"+ str(miesiac) +"/"+str(random.randint(1970,2000))


  
zapisjson("birthday", generate_dict())

def otworz_slownik():
    urodziny ={}
    with open("birthday.json", "r") as f:
        urodziny = json.load(f)
    wybor = int(input("Podaj: 1 jesli chcesz znalezc osobe, 2 jesli chcesz dodac osobe, 3 jesli chcesz sprawdzic ile osob urodzilo sie w kazdym z miesiecy: "))
    if wybor == 1:
        znajdz_osobe(urodziny)
    elif wybor == 2:
        temp = dodaj_do_slownika()
        urodziny[temp[0]+" " + temp[1]] = temp[2]
        zapisjson("birthday", urodziny)
    elif wybor == 3:
        zlicz_miesiace(urodziny)
        
def znajdz_osobe(urodziny):
    for key, value in urodziny.items() :
        print (key)
    wybor = input("\nPodaj imie i nazwisko osoby, ktorej date urodzin chcesz poznac: ")
    print(urodziny[wybor]) if wybor in urodziny else print("Brak takiej osoby")

def dodaj_do_slownika():
    print("Format podawania danych: Imie Nazwisko dzien/miesiac/rok")
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    data = input("Podaj date: ")
    return [imie.strip(), nazwisko.strip(), data.strip()]
    
def zlicz_miesiace(urodziny):
    miesiace = []
    for key, value in urodziny.items():
        miesiace.append(int(value.split("/")[1]))
    spis_miesiecy = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]
    months = [spis_miesiecy[i-1] for i in miesiace]
    from collections import Counter
    c = Counter(months)
    print(c)
    
#zadanie 36 wykresy
def zlicz_miesiace(urodziny):
    miesiace = []
    for key, value in urodziny.items():
        miesiace.append(int(value.split("/")[1]))
    spis_miesiecy = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]
    #miesiace = sorted(miesiace)
    
    from collections import Counter
    c = Counter(miesiace)
    print(type(c))
    c = sorted(c.items())

    print(c)
    print(type(c))
    
    from bokeh.plotting import figure, show, output_file
    output_file("plot.html")
    x_categories = spis_miesiecy
    x = [spis_miesiecy[key[0]-1] for key in c]
    y = [value[1] for value in c]
    print(x)
    print(y)

    p = figure(x_range = x_categories, width=1000, height=600)
    p.vbar(x=x, top=y, width=0.5)

    show(p)
    
    
#zadanie 38 i 39 f stringi
import datetime
wiek = int(input("Ile masz lat? "))
now = datetime.datetime.now()
print(f"Masz {wiek} lat i w roku {now.year + 100 - wiek} bedziesz mial 100 sto lat")

#zadanie 40 error checking

import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
    try:  
        guess = int(input("Guess a number between 1 and 9: "))
    except ValueError:
        print("Podaj cyfre!!!")
        continue
    if (guess < 1 or guess > 9):
        print(f"Liczba {guess} nie miesci sie w przedziale 1-9") 
    else:
        number_of_guesses += 1 
    if guess == number:
        break
print(f"You needed {number_of_guesses} guesses to guess the number {number}")