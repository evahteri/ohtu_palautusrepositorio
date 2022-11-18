import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
from kirjanpito import Kirjanpito

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.kirjanpito = Kirjanpito()

        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()
    
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            
            if tuote_id == 2:
                return 10
            
            if tuote_id == 3:
                return 0
            
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 10)
            if tuote_id == 3:
                return Tuote(3, "jäätelö", 7)
        
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        def pankki_lisää_tapahtuma(viitenumero=42, tililta="12345", tilille="33333-44455", summa=5):
            self.kirjanpito.lisaa_tapahtuma(f"tilisiirto: tililtä {tililta} tilille {tilille} viite {viitenumero} summa {summa}e"
        )

        self.pankki_mock.tilisiirto.side_effect = pankki_lisää_tapahtuma()
        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, 
        self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikein_kaksi_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 15)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikein_kaksi_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikein_kaksi_tuotetta_toinen_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_aloita_asionti_nolla_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("lauri", "11111")

        self.pankki_mock.tilisiirto.assert_called_with("lauri", 42, "11111", "33333-44455", 10)

    def test_joka_tapahtumalle_uusi_viitenumero(self):
        uusi_viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        uusi_kauppa_mock = Kauppa(self.varasto_mock, self.pankki_mock, 
        uusi_viitegeneraattori_mock)

        uusi_kauppa_mock.aloita_asiointi()
        uusi_kauppa_mock.lisaa_koriin(1)
        uusi_kauppa_mock.tilimaksu("pekka", "12345")

        self.assertEqual(uusi_viitegeneraattori_mock.uusi.call_count, 1)

        uusi_kauppa_mock.aloita_asiointi()
        uusi_kauppa_mock.lisaa_koriin(2)
        uusi_kauppa_mock.tilimaksu("lauri", "11111")

        self.assertEqual(uusi_viitegeneraattori_mock.uusi.call_count, 2)
    
        uusi_kauppa_mock.aloita_asiointi()
        uusi_kauppa_mock.lisaa_koriin(2)
        uusi_kauppa_mock.tilimaksu("matias", "33311")

        self.assertEqual(uusi_viitegeneraattori_mock.uusi.call_count, 3)

    def test_poista_ostoskorista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)

        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kirjanpitoon_lisätään(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.assertEqual(self.kirjanpito.tapahtumat, ["tilisiirto: tililtä 12345 tilille 33333-44455 viite 42 summa 5e"] )
