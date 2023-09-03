import sys
from kitapekle import KitapEkleEkrani
from anaekran_ui import Ui_AnaEkran
from PyQt5.QtWidgets import *



class Anaekran(QMainWindow, Ui_AnaEkran):
    def __init__(self):
        super(Anaekran, self).__init__()
        self.karsilama()

    def karsilama(self):
        self.setupUi(self)
        self.actionKitap_Ekle.triggered.connect(self.kitap_ekle)
        self.actionKitap_Listesi.triggered.connect(self.kitap_liste)
        self.actionKitap_G_ncelle.triggered.connect(self.kitap_guncelle)
        self.actionKitap_Sil.triggered.connect(self.kitap_silme)

    def cikis(self):
        print("çıkış tıklandı")

    def kitap_silme(self):
        print("kitap silindi")

    def kitap_ekle(self):
        self.setCentralWidget(KitapEkleEkrani(self.k_id))

    def kitap_liste(self):
        print("kitap listelemeye tıklandı")
        self.karsilama()

    def kitap_guncelle(self):
        print("kitap güncelle")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Anaekran()
    pencere.show()
    sys.exit(app.exec_())
