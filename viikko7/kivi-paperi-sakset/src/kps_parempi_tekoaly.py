
from tekoaly_parannettu import tekoaly_parannettu
from kivipaperisakset import KiviPaperiSakset


class KPSParempiTekoaly(KiviPaperiSakset):

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = tekoaly_parannettu.anna_siirto()
        tekoaly_parannettu.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto

