import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation

plik = open('Rzut_Ukosny_dane.txt','w')

f ="Program sluzy do wizualizacji rzutu ukosnego.\n" \
    "\nRzut ukosny to zlozenie dwoch ruchow: jednostajnego w poziomie i jednostajnie zmiennego w pionie,\n" \
    "gdzie podczas wznoszenia ciala wystepuje ruch jednostajnie opozniony, natomiast w czasie spadku - jednostajnie przyspieszony.\n" \
    "Cialu umieszczonemu na poziomie poczatkowym nadaje sie predkosc poczatkowa, skierowana pod katem alfa do tego poziomu.\n" \
    "Cialo w rzucie ukosnym porusza sie po paraboli z ramionami skierowanymi do dolu.\n"\
    "\nProgram umozliwia ustawienie wysokosci poczatkowej, predkosci poczatkowej oraz kata,\n"\
    "pod ktorym wyrzucone zostanie cialo.\n"\
    "Po wprowadzeniu wszystkich danych, program wyswietli wykres rzutu, jego animacje oraz zapisze dane do pliku.\n"
print(f)
plik.write(f)


def rzut_ukosny():
    g = 9.81
    print("Proszę o wprowadzenie:\n")

    while 1:
        try:
            h = float(input("1.Wysokości początkowej:\n"
                  "jednostka: metry [m]\n"))
            while h < 0 or h > 15:
                print("Błędne dane: podaj wartość liczbową większą od 0 i mniejszą od 15.")
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
            while V0 < 0 or V0 > 12:
                print("Błędne dane: podaj wartość liczbową większą od 0 i mniejszą od 12.")
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

    print('\nWysokosc poczatkowa:',h,'m\nPredkosc poczatkowa:',V0,'m/s\nKat wyrzutu:',a,file=plik)
    print('Dla podanych parametrow zasieg rzutu wynosi:', round(z, 2), 'm, wysokosc maksymalna:', round(hmax, 2), 'm.', file=plik)

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
    plt.savefig("wykres_rzutu_ukosnego.png")
    plt.show()


    t_min = 0
    t_max = (V0*c/g)+((2*hmax/g)**(1/2))
    dt = 0.05
    t = np.arange(t_min, t_max+dt, dt)

    fig = plt.figure()
    ax = fig.add_subplot()
    line = plt.plot(x, y, color='#f0adcf')
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    ax.set_ylabel('y[m]', fontsize=12)
    ax.set_xlabel('x[m]', fontsize=12)
    plt.title('Animacja rzutu ukośnego', fontsize=20)
    particle, = plt.plot(x, y, marker='o', color='#8c0047')
    traj, = plt.plot(x, y, color='#ab0a5c', alpha=0.8)

    czasomierz = 'czas = %.2fs'
    time_text = ax.text(0.75, 0.8, '', transform=ax.transAxes)

    print('Czas rzutu:', round(t_max,2), 's', file=plik)

    def animacja(i):
        particle.set_data(x[i], y[i])
        traj.set_data(x[:i + 1], y[:i + 1])
        time_text.set_text(czasomierz % (i * dt))
        return particle, traj, time_text


    ani = FuncAnimation(fig, animacja, np.arange(0, len(t)), interval = 70, repeat = False)
    plt.show()

    plik.close()

rzut_ukosny()

