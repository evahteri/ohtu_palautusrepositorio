from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tavaroiden_lukumäärä = 0
        self.tavarat = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.tavaroiden_lukumäärä
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for i in self.tavarat:
            hinta += i.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        löytyi = False
        uusi_ostos = Ostos(lisattava)
        for ostos in self.tavarat:
            if ostos.tuotteen_nimi() == uusi_ostos.tuotteen_nimi():
                löytyi = True
                ostos.muuta_lukumaaraa(1)
        if not löytyi:
            self.tavarat.append(uusi_ostos)
        self.tavaroiden_lukumäärä += 1

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        indeksi = 0
        for ostos in self.tavarat:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                maara = ostos.lukumaara()
                if maara > 1:
                    ostos.muuta_lukumaaraa(-1)
                if maara == 1:
                    self.tavarat.pop(indeksi)
            indeksi += 1
        self.tavaroiden_lukumäärä -= 1

    def tyhjenna(self):
        self.tavaroiden_lukumäärä = 0
        self.tavarat = []

    def ostokset(self):
        return self.tavarat
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
