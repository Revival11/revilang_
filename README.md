q# Revilang Interpreter

---

## Hak Cipta
© 2024 Revival Fanuel Mumu. Semua hak dilindungi. Revilang adalah bahasa pemrograman yang dirancang untuk memberikan pengalaman pemrograman yang intuitif dan mudah dipahami.

---

## Fitur Revilang
Revilang memiliki berbagai fitur yang mendukung berbagai fungsionalitas pemrograman, termasuk:


1. **Komentar**:
   - Mendukung komentar satu baris dengan `#-` dan komentar beberapa baris dengan `#` di awal dan di akhir komentar.

2. **Deklarasi Variabel**:
   - Variabel dapat dideklarasikan menggunakan sintaks `var +name_variable`.

3. **Pengubahan Variabel**:
   - Mengubah nilai variabel dengan hanya menyebutkan nama variabel.

4. **Event**:
   - Mendukung input pengguna dan output ke konsol.

5. **Operasi Matematika**:
   - Mendukung operasi matematika dasar.

6. **Kelas**:
   - Mendukung pembuatan kelas.

7. **Looping**:
   - Mendukung loop `for` dan `while`.

8. **Operator Perbandingan dan Logika**:
   - Mendukung operator perbandingan dan logika seperti `==`, `!=`, `>`, `<`, `&&`, `||`.

9. **input**
   - mendukung pengguna memasukan sebuah string atau number.

---

Berikut adalah contoh **Sintaks Lengkap Revilang** dengan penggunaan fitur seperti deklarasi variabel, operasi matematika, kelas, loop, perbandingan logika, dan input:

# **Contoh Sintaks Lengkap Revilang**

## **1. Deklarasi Variabel**

### Deklarasi variabel string
var +name = "John"            

### Deklarasi variabel number
var +age = 25                

### Deklarasi variabel boolean
var +isStudent = true        

### Deklarasi array
var +numbers = [1, 2, 3, 4]  

### Deklarasi objek
var +person = {name = "Alice", age = 30}


## **2. Input dan Output**

### Mendapatkan input string dari pengguna
event.console-output("Masukkan nama Anda: ")
var +input_name = event.input(str("Masukkan nama Anda: "))  

### Mendapatkan input number dari pengguna
event.console-output("Masukkan umur Anda: ")
var +input_age = event.input(number("Masukkan umur Anda: "))  

### Menampilkan hasil input ke konsol
event.console-output("Nama Anda adalah: " + input_name)
event.console-output("Umur Anda adalah: " + input_age)


## **3. Operasi Matematika**

### Operasi matematika dasar
var +number1 = 10
var +number2 = 20
var +sum = number1 + number2   # Penjumlahan
var +product = number1 * number2  # Perkalian

event.console-output("Hasil penjumlahan: " + sum)
event.console-output("Hasil perkalian: " + product)

### Operasi matematika menggunakan fungsi
var +hasil_sin = math.sin(3.14)
event.console-output("Hasil sinus dari 3.14: " + hasil_sin)

## **4. Kelas**

### Definisi kelas
property.all /Person {
    var +name = "John"
    var +age = 30
    event.console-output("Nama saya " + name + " dan umur saya " + age)
}

### Definisi kelas dengan pengubahan variabel
property.variable /class_variable {
    var +name = "Jhon"
    name = "Joko"  # Mengubah nilai variabel dalam kelas
    event.console-output("Nama baru adalah " + name)
}

## **5. Loop (Perulangan)**
plaintext
### Loop for sederhana untuk iterasi array
var +numbers = [1, 2, 3, 4, 5]

loop.for (var +i + 0(i <= 4)) {
    event.console-output("Angka: " + numbers[i])
}

### Loop while menggunakan kondisi logika
var +counter = 0
loop.as-much (counter < 5) {
    event.console-output("Counter: " + counter)
    counter = counter + 1
}

## **6. Kondisi dan Operator Logika**

### Kondisi if-else sederhana
var +number = 10

if /(number > 5) {
    event.console-output("Number lebih besar dari 5")
} elif /(number == 5) {
    event.console-output("Number sama dengan 5")
} else /(number < 5) {
    event.console-output("Number lebih kecil dari 5")
}

---

### Cara Menjalankan

1. Setelah mendownload interpreter **Revilang**, pindahkan file interpreter tersebut ke folder tempat kamu ingin mencoba menjalankan kode.
2. Buat file dengan format **.rl** di folder yang sama. Tuliskan kode yang ingin kamu uji di file tersebut.
3. Buka terminal, kemudian jalankan perintah berikut:
    python3 interpreter.py file_name.rl

   **Catatan**: Pastikan kamu sudah menginstall **Python** di sistemmu.

4. Lihat output di terminal. Jika ada kesalahan atau masalah saat menjalankan kode, mohon maaf dan jangan ragu untuk memberikan feedback kepadaku di nomor **081543489053**.
