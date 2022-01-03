import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation


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
                  "jednostka: metry [m]\n"))
            while h < 0:
                print("Błędne dane: podaj wartość liczbową większą od 0.")
                h = float(input("1.Wysokości początkowej:\n"
                                "jednostka: metry [m]\n"))
                break
            break
        except ValueError:
            print("Błędne dane: podaj wartość liczbową.")

    while 2:
        try:
            V0 = float(input("2.Prędkości początkowej:\n"
          "jednostka: metry na sekundę [m/s]\n"))
            while V0 < 0:
                print("Błędne dane: podaj wartość liczbową większą od 0.")
                V0 = float(input("2.Prędkości początkowej:\n"
                                 "jednostka: metry na sekundę [m/s]\n"))
                break
            break
        except ValueError:
            print("Błędne dane: podaj wartość liczbową.")

    while 3:
        try:
            a = float(input("3.Kąta, pod którym ciało zostanie wyrzucone:\n"
                            "UWAGA: wybierz kąt z przedziału <0, pi/2>\n"))
            while a > (math.pi/2) or a < 0:

                print("Błędne dane: podaj wartość liczbową z przedziału <0, pi/2>.")
                a = float(input("3.Kąta, pod którym ciało zostanie wyrzucone:\n"
                                "UWAGA: wybierz kąt z przedziału <0-pi/2>\n"))
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
    hmax = ((V0*V0*c*c)/(2*g))+h
    print('Dla podanych parametrów zasięg rzutu wynosi:',round(z,2),'m, wysokość maksymalna:',round(hmax,2),'m.')


    plt.plot(x, y, color='m', lw = 2)
    plt.xlim(0,20)
    plt.ylim(0, 20)
    plt.xlabel('x[m]', fontsize=12)
    plt.ylabel('y[m]', fontsize=12)
    plt.title('Wykres rzutu ukośnego',fontsize=20)
    plt.grid(True)
    label = (round((z/2),2),round((hmax),2))
    plt.annotate(label,
                    xy=(z/2, hmax),
                    xytext=(z/2, hmax+1),
                    arrowprops={'arrowstyle': '->'}
                    )

    plt.show()


    fig = plt.figure()
    ax = fig.add_subplot()
    line, = plt.plot(x, y)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    ax.set_ylabel('x[m]', fontsize=12)
    ax.set_xlabel('y[m]', fontsize=12)
    particle, = plt.plot(x, y, marker='o')
    traj, = plt.plot(x, y)

    def animacja(i):
        particle.set_data(x[i], y[i])
        traj.set_data(x[:i + 1], y[:i + 1])
        return particle, traj

    ani = FuncAnimation(fig, animacja, np.arange(0, 50), interval=25)
    plt.show()


rzut_ukosny()
