# Scraping Data YouTube

Google menyediakan YouTube Data API v3 yang memungkinkan Anda mengakses data publik YouTube, termasuk video, channel, playlist, dan banyak lagi secara legal. Ini adalah cara yang lebih tepat untuk mengambil data daripada menggunakan teknik scraping langsung, karena YouTube memiliki aturan ketat terkait scraping.

<br>

Dengan YouTube Data API v3, Anda dapat mengakses berbagai data terkait channel, seperti:

- Daftar video dalam sebuah channel.
- Metadata video (judul, deskripsi, jumlah like, komentar, dll).
- Playlist.
- Statistik channel (jumlah subscriber, jumlah views, dll).

## Get API KEY

- Masuk ke Google Cloud Console
- Buat proyek baru (atau gunakan yang sudah ada)
- Cari dan aktifkan YouTube Data API v3
- Create credential public API

## Setup Project

Project ini menggunakan bahasa pemrograman Python pada VS Code dan dengan OS Windows.

- Buat folder project
- Buat Virtual Environment dengan melakukan perintah `python -m venv .venv` pada terminal vs code
- Aktifkan virtual environment dengan perintah `.venv\Scripts\Activate`. Jika terjadi error permission, lakukan perintah `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` kemudian aktifkan lagi.
- Jika sudah aktif, install beberapa library yang dibutuhkan seperti pandas dan google-api-python-client dengan perintah `pip install google-api-python-client pandas`
- Setelah library diinstall, jalankan project.
