import numpy as np
import matplotlib.pyplot as plt
import math

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

    while 1:
        try:
            h = float(input("1.Wysokości początkowej:\n"
                  "jednostka: metry [m]"))
            while h < 0:
                print("Błędne dane: podaj wartość liczbową większą od 0.")
                h = float(input("1.Wysokości początkowej:\n"
                                "jednostka: metry [m]"))
                break
            break
        except ValueError:
            print("Błędne dane: podaj wartość liczbową.")

    while 2:
        try:
            V0 = float(input("2.Prędkości początkowej:\n"
          "jednostka: metry na sekundę [m/s]"))
            while V0 < 0:
                print("Błędne dane: podaj wartość liczbową większą od 0.")
                V0 = float(input("2.Prędkości początkowej:\n"
                                 "jednostka: metry na sekundę [m/s]"))
                break
            break
        except ValueError:
            print("Błędne dane: podaj wartość liczbową.")

    while 3:
        try:
            a = float(input("3.Kąta, pod którym ciało zostanie wyrzucone:\n"
                            "UWAGA: wybierz kąt z przedziału <0, pi/2>"))
            while a > (math.pi/2) or a < 0:

                print("Błędne dane: podaj wartość liczbową z przedziału <0, pi/2>.")
                a = float(input("3.Kąta, pod którym ciało zostanie wyrzucone:\n"
                                "UWAGA: wybierz kąt z przedziału <0-pi/2>"))
                break
            break
        except ValueError:
            print("Błędne dane: podaj wartość liczbową.")

    t = np.linspace(0,5,100)

    b = math.cos(a)
    c = math.sin(a)
    x = V0 * t * b
    y = h + (V0 * c * t - (g * t * t)/2)
    z = 2*V0*V0*c*b/g
    hmax = V0*V0*c*c/(2*g)
    print('Dla podanych parametrów zasięg rzutu wynosi:',z,'m, wysokość maksymalna:',hmax,'m.')


    plt.plot(x, y)
    plt.xlim(0,10)
    plt.ylim(0, 10)
    plt.show()

rzut_ukosny()
