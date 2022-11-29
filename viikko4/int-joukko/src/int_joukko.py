class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.lukujono:
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == len(self.lukujono):
                self.lukujono = self.lukujono + [0] * self.kasvatuskoko
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.lukujono.remove(n)
            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_taulukko(self, a_taulukko, b_taulukko):
        for i in range(0, len(a_taulukko)):
            b_taulukko[i] = a_taulukko[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            joukko.lisaa(i)

        for i in b_taulu:
            joukko.lisaa(i)

        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    joukko.lisaa(b_taulu[j])

        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            joukko.lisaa(i)

        for i in b_taulu:
            joukko.poista(i)

        return joukko

    def __str__(self):
        tuotos = "{"
        if self.alkioiden_lkm == 0:
            tuotos += "}"
        else:
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
        return tuotos
