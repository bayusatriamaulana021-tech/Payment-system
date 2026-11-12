"""Peragaan Tugas 3 (langkah 2): apa yang terjadi saat biaya_admin()
sudah menjadi method abstrak, tetapi plugin belum mengimplementasikannya.

Kelas di bawah meniru kondisi plugin SEBELUM biaya_admin() diisi.
"""
from core.base import PaymentMethod
from core.utils import buat_id


class TransferBankLama(PaymentMethod):
    def validasi(self, jumlah):
        return True

    def bayar(self, jumlah):
        return buat_id("TRF")


class EWalletLama(PaymentMethod):
    def validasi(self, jumlah):
        return True

    def bayar(self, jumlah):
        return buat_id("EWL")


class QRISLama(PaymentMethod):
    def validasi(self, jumlah):
        return True

    def bayar(self, jumlah):
        return buat_id("QRS")


for kelas in (TransferBankLama, EWalletLama, QRISLama):
    try:
        kelas("uji")
    except TypeError as e:
        print(f"{kelas.__name__}: TypeError -> {e}")
