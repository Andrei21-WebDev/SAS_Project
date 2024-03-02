import pandas as pd
import matplotlib.pyplot as plt

# Liste si dictionare
# 1 Sa se creeze o lista de liste ce contin modelul masinii, pretul si cantitatea. Sa se calculeze valoarea masinilor si sa se afiseze lista sortata
l = []
l1 = ["S Class", 34948, 38]
l2 = ["G Class", 61948, 27]
l3 = ["A Class", 32980, 74]
l.append(l1)
l.append(l2)
l.append(l3)
val1 = l1[1]*l1[2]
val2 = l2[1]*l2[2]
val3 = l3[1]*l3[2]
l1.insert(3, val1)
l2.insert(3, val2)
l3.insert(3, val3)
l.sort(key=lambda x:x[3])

# print(l)

# 2 Sa se creeze un dictionar care sa aiba ca si cheie modelul masinii si ca valoare anul aparitiei. Sa se determine masina cea mai veche si cea mai noua din dictionar

cars = {"GLE Class" : 2018,
        "S Class" : 2012,
        "SL Class" : 2011,
        "G Class" : 2019,
        "GLA Class" : 2017}

def min(cars):
    min = cars["GLE Class"]
    for car, year in cars.items():
        if year < min:
            min = year
            car_min = car

    return car_min

def max(cars):
    max = cars["GLE Class"]
    for car, year in cars.items():
        if year > max:
            max = year
            car_max = car

    return car_max

# print('Cea mai veche masina din dictionar este ' + f'{min(cars)}')
# print('Cea mai noua masina din dictionar este ' + f'{max(cars)}')


# Definirea si apelarea unor functii

# 3 Sa se determine media consumului pentru urmatoarea lista de consumuri prin apelarea unei functii
consumuri = [32.1, 61.4, 28, 30.4, 30.1]

def medie_consum(list):
    return sum(list)/len(list)

# print('Media consumului este ' + f'{medie_consum(consumuri)}')


# 4 Sa se defineasca o functie care determina ce tip de consum are o masina in functie de capacitatea cilindrica
def cat_consuma(consum, cc):
    if cc > 3.0 and consum > 30:
        print("Masina consuma putin")
    elif cc < 3.0 and consum < 30:
        print("Masina consuma mult")
    else: print("Masina are un consum balansat")

# cat_consuma(25.2, 2.8)
# cat_consuma(28, 5.5)
# cat_consuma(30.4, 4)

# 5 Sa definseasca o functie care face conversia unei liste de consumuri mila/galon catre litru/100 kilometri
def convert_mpg_to_lpk(mpg):
    lpk = 235.215 / mpg
    return lpk

def consum_convert(list):
    for i in range(len(list)):
        list[i] = round(convert_mpg_to_lpk(list[i]), 2)
    return list

consumuri = consum_convert(consumuri)
# print('Consum in litru/100km: ' + f'{consumuri}')

# Seturi
# 6 Sa se realizeze intersectia dintre doua seturi si diferenta dintre ele

set1 = {"S Class", "C Class", "SL Class"}
set2 = {"GLA Class", "G Class", "S Class", "A Class", "SL Class"}
intersectie = set1.intersection(set2)
diferenta = set2.difference(set1)

# print('Intersectie de seturi: ' + f'{intersectie}')
# print('Diferenta dintre setul 2 si setul 1: ' + f'{diferenta}')

# Importul fisierelor csv

usedCarsList = pd.read_csv('UsedCarList.csv')
carSales = pd.read_csv('car_sales_data.csv', index_col=0)

# print(usedCarsList)
# print(carSales)

# Acesarea datelor cu loc si iloc
# 7 Sa se returneze coloanele 3,4 si 7 pentru randurile 2,7,18,74 si 324. Totodata, sa se determine numele, data si pretul de cumparare pentru primii 20 de clienti
# print(usedCarsList.iloc[[2,7,18,74,324], [3,4,7]])
# print('\n')
# print(carSales.loc[:20, "Nume Client":"Pret Cumparare"])

# 8 Afiseaza clientii care au cumparat masina in anul 2022 la un pret mai mic de 25000

carSales['Data Cumparare'] = pd.to_datetime(carSales['Data Cumparare'], format='%m/%d/%Y')
# print(carSales.loc[(carSales["Data Cumparare"].dt.year == 2022) & (carSales["Pret Cumparare"] < 25000), "Nume Client":"Pret Cumparare"])

# 9 Afiseaza masinile cu combustibil Petrol care inregistreaza un numar de mile intre 25000 si 50000

# print(usedCarsList.loc[(usedCarsList["Combustibil"] == "Petrol") & (usedCarsList["Nr mile"].between(25000, 50000, inclusive='both')), "Model":"Combustibil"])

# Modificarea datelor in pachetul pandas
# 10 Scade pretul cu 15% unde taxele sunt mai mari de 250

preturi_gasite = usedCarsList.loc[usedCarsList["Taxe"] > 250, "Pret"]
# print(preturi_gasite)
preturi_reduse = preturi_gasite - preturi_gasite*0.15
# print(preturi_reduse)

# Functii de grup
# 11 Sa se afiseze capacitatea cilindrica maxima, minima, medie si masinile care detin maximele si minimele

# print('Capacitate maxima: ', usedCarsList["Capacitate cilindrica"].max())
# print('Capacitate minima: ', usedCarsList["Capacitate cilindrica"].min())
# print('Capacitate medie: ', round(usedCarsList["Capacitate cilindrica"].mean(), 2))
#
# print('\n\n' , usedCarsList.loc[usedCarsList["Capacitate cilindrica"] == usedCarsList["Capacitate cilindrica"].max(), ["Model", "Capacitate cilindrica"]])
# print('\n' , usedCarsList.loc[usedCarsList["Capacitate cilindrica"] == usedCarsList["Capacitate cilindrica"].min(), ["Model", "Capacitate cilindrica"]])

# Tratarea valorilor lipsa
# 12 Sa se inlocuiasca cu null valorile hibrid si apoi sa se transforme in electric prin tratare de valori lipsa

# usedCarsList.loc[usedCarsList["Combustibil"] == "Hybrid"] = None
# print(usedCarsList["Combustibil"].fillna("Electric"))

# Stergerea coloanelor si inregistrarilor
# 13 Stergeti coloanele Taxe si Nr Mile si salvati noul dataframe intr-un alt csv

df_nou = usedCarsList.drop(["Nr mile", "Taxe"], axis=1)
df_nou.to_csv("UsedCarsListNou.csv", index=False)

# 14 Stergeti masinile automate si salvati noul dataframe intr-un csv

masini_automate = usedCarsList.loc[usedCarsList["Transmisie"] == "Automata"]
df_fara_masini_automate = usedCarsList.drop(masini_automate.index, axis=0)
df_fara_masini_automate.to_csv("UsedCarsNoAutomatic.csv", index=False)

# Prelucrari statistice, gruparea si agregarea datelor
# 15 Afisati totalul de masini listate dupa tipurile de combustibil pentru fiecare reprezentanta
# print(usedCarsList.groupby(["Id Reprezentanta", "Combustibil"]).size())

# 16 Afisati valoarea totala a masinilor pentru fiecare reprezentanta
# print(usedCarsList.groupby(by="Id Reprezentanta")["Pret"].sum())

# 17 Afisati pentru fiecare reprezentanta, in functie de tipurile de transmisie, cel mai des model de masina, media numarului de mile si maximul de consum
# pd.set_option("display.max_columns", None)
# print(usedCarsList.groupby(["Id Reprezentanta", "Transmisie"]).agg({"Model": lambda x:x.mode(),
#                                                                     "Nr mile": "mean",
#                                                                     "Consum": "min"}))


# Prelucrarea seturilor de date cu merge / join
# 18 Afisati rezultatul combinarii cu fisierul Orase.csv al fisierului UsedCarList.csv si obtineti modelul cel mai vandut pe oras

orase = pd.read_csv("Orase.csv", index_col=0)

rez1 = pd.merge(usedCarsList, orase, left_on="Id Reprezentanta", right_index=True)
# print(rez1)
# print(rez1.groupby("Oras Reprezentanta")["Model"].agg(lambda x:x.mode()))

# Reprezentare grafica a datelor cu pachetul matplotlib
# 19 Afisati intr-un grafic de tip bar numarul de masini cumparate in fiecare oras de catre clienti
# rez2 = pd.merge(carSales, orase, left_on="Id Reprezentanta", right_index=True)
# masini_cumparate = rez2.groupby(by="Oras Reprezentanta").size()
# print(masini_cumparate)
# masini_cumparate.plot(kind='barh')
# plt.title("Numarul de masini cumparate in fiecare oras")
# plt.show()


# 20 Afisati intr-un grafic de tip pie procentul tipurilor de transmisie a masinilor vandute
# proc_transmisie = usedCarsList.groupby(by="Transmisie").size()
# plt.pie(proc_transmisie, labels=proc_transmisie.index.values, autopct='%1.1f%%')
# plt.show()

