"""Eksperimen tambahan Tugas 2.

1) Protocol TANPA @runtime_checkable -> isinstance() memunculkan TypeError.
2) WhatsAppRusak: kirim(self) tanpa parameter -> isinstance() tetap True.
"""
from typing import Protocol

from core.protocols import Notifier


class TanpaDekorator(Protocol):
    """Sama seperti Notifier, tetapi TANPA @runtime_checkable."""

    def kirim(self, penerima: str, pesan: str) -> None: ...


class WhatsAppRusak:
    def kirim(self):  # sengaja tanpa parameter penerima dan pesan
        print("[WHATSAPP]")


print("--- Eksperimen: isinstance() tanpa runtime_checkable ---")
try:
    isinstance(WhatsAppRusak(), TanpaDekorator)
except TypeError as e:
    print("TypeError:", e)

print()
print("--- Eksperimen: kirim(self) tanpa parameter ---")
print("isinstance(WhatsAppRusak(), Notifier) ->",
      isinstance(WhatsAppRusak(), Notifier))
print("(runtime hanya mengecek NAMA method, bukan tanda tangannya)")
