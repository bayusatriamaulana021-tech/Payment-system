"""Pengujian Tugas Mandiri 1 sampai 3."""
from core.notifiers import ConsoleNotifier, TelegramNotifier
from core.processor import PaymentProcessor
from core.protocols import Notifier
from core.registry import buat_metode, daftar_plugin
from core.utils import rupiah
from plugins import muat_semua_plugin
from plugins.ewallet import EWallet
from plugins.qris import QRIS
from plugins.transfer_bank import TransferBank

muat_semua_plugin()
pelanggan = "mahasiswa@utr.ac.id"

print("=== Tugas 1: plugin QRIS ===")
print("Plugin terdaftar:", daftar_plugin())
pemroses = PaymentProcessor(ConsoleNotifier())
pemroses.checkout(buat_metode("qris"), 4_000_000, pelanggan)
pemroses.checkout(buat_metode("qris"), 5_000_000, pelanggan)  # total > batas

print()
print("=== Tugas 2: TelegramNotifier tanpa pewarisan ===")
print("Basis kelas TelegramNotifier:", TelegramNotifier.__bases__)
print("isinstance(TelegramNotifier(), Notifier):",
      isinstance(TelegramNotifier(), Notifier))
pemroses_tg = PaymentProcessor(TelegramNotifier())
pemroses_tg.checkout(QRIS(), 50_000, "@mahasiswa")

print()
print("=== Tugas 3: biaya admin tiap plugin ===")
for metode, jumlah in [
    (TransferBank(saldo=1_000_000), 250_000),
    (EWallet(saldo=1_000_000), 300_000),
    (QRIS(), 50_000),
]:
    print(f"{metode.nama:<20} jumlah {rupiah(jumlah):>10} "
          f"-> biaya admin {rupiah(metode.biaya_admin(jumlah))}")
