from kitapekleform import Ui_KitapEkleForm
from PyQt5.QtWidgets import *
import sys
import veritabani_06 as baglanti


class KitapEkleEkrani(QWidget, Ui_KitapEkleForm):
    def __init__(self,k_id):
        super().__init__()
        self.k_id = k_id
        self.kayitButonu.clicked.connect(self.fGiris)

    def fbaslat(self):
        self.setupUi(self)
        self.kayitButonu.clicked(self.kitap_ekle)

    def kitap_ekle(self):
        k_adi = self.kitapAdiLineEdit.text()
        k_yazari = self.kitapYazariLineEdit.text()
        k_durum = self.okunmaDurumuCheckBox.checkState()
        k_begeni = self.begeniDurumuLineEdit.itemText()
        baglanti.ekle(k_adi, k_yazari, k_durum, k_begeni, self.k_id)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = KitapEkleEkrani()
    pencere.show()
    sys.exit(app.exec_())
