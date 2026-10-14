#Zadanie 1 (rozgrzewka). Zadeklaruj zmienne: imię, wiek, wzrost w metrach (float). Wypisz zdanie w stylu Anna, 23 lata, wzrost: 1.68 m używając f-stringa. Dodatkowo wypisz typ każdej zmiennej.

# imie = "Anna"
# wiek = "20"
# wzrost = 1.73

# print(f"{imie} ma {wiek} lat oraz {wzrost} wzrostu")



#Zadanie 2. Masz dane: cena_netto = "249.90" i vat = "23" (oba jako str, jakby przyszły z pliku). Policz cenę brutto i wypisz ją w formacie Cena brutto: 307.38 PLN. Zwróć uwagę na konwersję typów.

# cena_netto = "249.90"
# vat = "23"

# cena_brutto = round(float(cena_netto) / int(vat),2)
# print(cena_brutto)



#Zadanie 3. Napisz program, który pyta użytkownika (input()) o liczbę wyprodukowanych sztuk i liczbę sztuk wadliwych, a potem wypisuje procent braków z jednym miejscem po przecinku.
#  Co się stanie, jeśli użytkownik wpisze 0 jako liczbę wyprodukowanych? Napisz w komentarzu, co zauważyłeś (na razie nie musisz tego obsługiwać).

# x = int(input("Podaj liczbe wyprodukowanych sztuk "))
# y = int(input("Podaj liczbe wadliwych sztuk "))

# if x == 0:
#     print("Błąd")
# else:
#     print(f"{round((y * 100 / x),2)}%")



#Zadanie 4 (automatyzacja). Dane zmiany produkcyjnej: data = "2026-10-12", linia = "L3", wyprodukowano = 1840, braki = 37, plan = 2000. Wygeneruj tekst krótkiego raportu, który wypisze się w 4 liniach:

# Raport zmianowy 2026-10-12 | Linia L3
# Wyprodukowano: 1,840 szt. (92.0% planu)
# Braki: 37 szt. (2.0%)
# Różnica do planu: -160 szt.

# Dodatkowo zapisz ten tekst do pliku, którego nazwa zawiera datę i linię, np. raport_2026-10-12_L3.txt (nazwę też zbuduj f-stringiem; podpowiedź: open(nazwa, "w", encoding="utf-8"), 
# to nasz pierwszy kontakt z plikami, więc możesz poszukać składni).

raport = [
    "Raport zmianowy 2026-10-12 | Linia L3", 
    "Wyprodukowano: 1,840 szt. (92.0% planu)", 
    "Braki: 37 szt. (2.0%)",
    "Różnica do planu: -160 szt."
    ]

with open("dane.txt", "w", encoding="utf-8") as plik:
    for tekst in raport:
        plik.write(tekst + "\n")

with open("dane.txt", "r", encoding="utf-8") as plik:
    tekst = plik.read()

print(tekst)