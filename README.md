## menjalankan project monolith dan microservis 
1.Masuk ke folder project:

```bash
cd ~/praktikum-monolith-microservices
```

Jika project berada di folder lain, sesuaikan lokasi foldernya.

2.membuat virtual environment

 Buat virtual environment Python dengan perintah:
```bash
python3 -m venv venv
```
Aktifkan virtual environment:
```bash
source venv/bin/activate
```
Jika berhasil, biasanya akan muncul (venv) di bagian awal terminal.

3.Install Library

Install Flask dan Requests:
```bash
pip install Flask requests
```

## Menjalankan Monolith

Jalankan aplikasi Monolith:
```bash
python3 monolith_app.py
```
Buka terminal baru untuk melakukan pengujian.

Menampilkan daftar buku
```bash
curl http://localhost:5000/books
```
Membuat pesanan
```bash
curl -X POST http://localhost:5000/orders \
-H "Content-Type: application/json" \
-d '{"book_id":1}'
```
Setelah order berhasil, stok buku akan berkurang.

## Menjalankan Microservices

1.Menjalankan Book Service

Buka terminal baru dan masuk ke folder project:
```bash
cd ~/praktikum-monolith-microservices
```
Aktifkan virtual environment:
```bash
source venv/bin/activate
```
Jalankan Book Service:
```bash
python3 book_service.py
```
Menampilkan semua buku

Buka terminal baru:
```bash
curl http://localhost:5001/books
```
menampilkan buku berdasarkan id
```bash
curl http://localhost:5001/books/1
```
## Menjalankan Order Service
Buka terminal baru dan masuk ke folder project:
```bash
cd ~/praktikum-monolith-microservices
```
Aktifkan virtual environment:
```bash
source venv/bin/activate
```
Jalankan Order Service:
```bash
python3 order_service.py
```

Membuat Order pada Microservices

Buka terminal baru dan jalankan:
```bash
curl -X POST http://localhost:5002/orders \
-H "Content-Type: application/json" \
-d '{"book_id":1}'
```
Order Service akan meminta data buku kepada Book Service melalui HTTP/API.

## Pengujian Fault Isolation
Untuk menguji fault isolation, hentikan Book Service dengan menekan:
```bash
ctrl + c
```
Kemudian biarkan Order Service tetap berjalan.

Coba membuat order kembali:
```bash
curl -X POST http://localhost:5002/orders \
-H "Content-Type: application/json" \
-d '{"book_id":1}'
```
Order Service tetap berjalan, tetapi akan memberikan pesan:
```bash
{
    "error": "Book Service sedang down!"
}
```
Hal tersebut menunjukkan bahwa Book Service dan Order Service merupakan service yang terpisah.
