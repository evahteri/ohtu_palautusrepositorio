from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KomentoTehdas:

    @staticmethod
    def pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja
    
    @staticmethod
    def pelaaja_vs_tekoaly():
        return KPSTekoaly
    
    @staticmethod
    def pelaaja_vs_parempi_tekoaly():
        return KPSParempiTekoaly
    
