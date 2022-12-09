from tekoaly import tekoaly
from kivipaperisakset import KiviPaperiSakset


class KPSTekoaly(KiviPaperiSakset):

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = tekoaly.anna_siirto()
        return tokan_siirto
