#Zadanie 1 (rozgrzewka). Zadeklaruj zmienne: imię, wiek, wzrost w metrach (float). Wypisz zdanie w stylu Anna, 23 lata, wzrost: 1.68 m używając f-stringa. Dodatkowo wypisz typ każdej zmiennej.

# imie = "Anna"
# wiek = "20"
# wzrost = 1.73

# print(f"{imie} ma {wiek} lat oraz {wzrost} wzrostu")

#Zadanie 2. Masz dane: cena_netto = "249.90" i vat = "23" (oba jako str, jakby przyszły z pliku). Policz cenę brutto i wypisz ją w formacie Cena brutto: 307.38 PLN. Zwróć uwagę na konwersję typów.

cena_netto = "249.90"
vat = "23"

cena_brutto = round(float(cena_netto) / int(vat),2)
print(cena_brutto)