from komento_tehdas import KomentoTehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        if vastaus.endswith("a"):

            peli_olio = KomentoTehdas.pelaaja_vs_pelaaja()
            peli_olio().pelaa()
        elif vastaus.endswith("b"):

            peli_olio = KomentoTehdas.pelaaja_vs_tekoaly()
            peli_olio().pelaa()

        elif vastaus.endswith("c"):

            peli_olio = KomentoTehdas.pelaaja_vs_parempi_tekoaly()
            peli_olio().pelaa()
        else:
            break


if __name__ == "__main__":
    main()
