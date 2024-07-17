import os
import mysql.connector

# Membuat koneksi ke database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dbPersediaan"
)

mycursor = db.cursor()

# Membersihkan layar konsol
os.system('cls')

# Menampilkan header
    hline = "-" * 40
print("\n\n")
print(" " * 20 + "INPUT DATA SUPLIER")
print(" " * 20 + hline)
print(" " * 28 + "Kode Suplier: ", end="")
    kode_suplier = input()
    print(" " * 28 + "Nama Suplier: ", end="")
    nama_suplier = input()
    print(" " * 28 + "Alamat: ", end="")
    alamat = input()
    print(" " * 28 + "Nomor Telpon: ", end="")
    nomor_telpon = input()
    print(" " * 20 + hline)

# Menyimpan data ke tabel
    sql = "INSERT INTO tblsuplier (kode_suplier, nama_suplier, alamat, nomor_telpon) VALUES (%s, %s, %s, %s)"
    val = (kode_suplier, nama_suplier, alamat, nomor_telpon)
    mycursor.execute(sql, val)
    db.commit()

    pesan = "Data Suplier Berhasil di Simpan"
    print(" " * 25 + pesan)
