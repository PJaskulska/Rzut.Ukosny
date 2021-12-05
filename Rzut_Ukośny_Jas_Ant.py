import numpy as np
import matplotlib.pyplot as plt

print("Program służy do wizualizacji rzutu ukośnego.\n"
      "\nRzut ukośny to złożenie dwóch ruchów: jednostajnego w poziomie i jednostajnie zmiennego w pionie,\n"
      "gdzie podczas wznoszenia ciała występuje ruch jednostajnie opóźniony, natomiast w czasie spadku - jednostajnie przyspieszony.\n"
      "Ciału umieszczonemu na poziomie początkowym nadaje się prędkość początkową, skierowaną pod katem alfa do tego poziomu.\n"
      "Ciało w rzucie ukośnym porusza się po paraboli z ramionami skierowanymi do dołu.\n"
      "\nProgram umożliwia ustawienie wysokości początkowej, prędkości początkowej oraz kąta,\n"
      "pod którym wyrzucone zostanie ciało.\n"
      "Po wprowadzeniu wszystkich danych, program wyświetli wykres rzutu, jego animację oraz zapisze dane do pliku.\n")

def rzut_ukosny():
    g = 9.81
    print("Proszę o wprowadzenie:\n")
    print("1.Wysokości początkowej:\n"
          "jednostka: metry [m]")
    h = float(input())
    print("2.Prędkości początkowej:\n"
          "jednostka: metry [m/s]")
    V0 = float(input())
    print("3.Kąta, pod którym ciało zostanie wyrzucone:\n"
          "UWAGA: wybierz kąt z przedziału (0-pi/2)")
    alfa = input()

    t = np.linspace(0,5,100) #można zmienić w trakcie tworzenia funkcji
rzut_ukosny()