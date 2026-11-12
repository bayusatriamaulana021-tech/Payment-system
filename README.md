<<<<<<< HEAD
# pbo-payment-system

Praktikum Pemrograman Berorientasi Objek: Merancang Sistem Pembayaran/Plugin dengan ABC dan Protocol.

- Nama  : Maulana Bayu Satria
- NIM   : 25130210050
- Kelas : B (Teknologi Informasi, Semester 3)
- Dosen : Syepry Maulana Husain, S.Kom, M.TI

## Cara menjalankan
Jalankan semua perintah dari folder `payment_system` (folder yang berisi `main.py`).

| Berkas | Isi |
| --- | --- |
| `tugas1.py` | Tugas 1: kontrak pembayaran dengan ABC |
| `tugas2.py` | Tugas 2: kontrak notifikasi dengan Protocol |
| `eksperimen_p2.py` | Eksperimen tambahan Tugas 2 |
| `tugas3.py` | Tugas 3: merangkai PaymentProcessor |
| `main.py` | Tugas 4: sistem plugin dengan registry |
| `uji_tugas.py` | Tugas Mandiri 1 sampai 3 |
| `tugas3_sebelum.py` | Peragaan Tugas 3: plugin gagal dibuat sebelum `biaya_admin()` diisi |

Struktur: `core/` (kontrak, registry, pemroses) dan `plugins/` (transfer, ewallet, qris).
Plugin baru cukup ditambahkan sebagai satu berkas di `plugins/` dengan dekorator `@register_plugin`.
=======
# Payment-system
>>>>>>> e324a3558fcd3ef903ea7c7a6cb259cab38dc6c6
