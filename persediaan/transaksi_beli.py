from kordinat import *
import mysql.connector
import os
import locale

# Set locale
locale.setlocale(locale.LC_ALL, '')

# Clear screen
if os.name == 'nt':  # Windows
    os.system('cls')
else:  # Unix/Linux/Mac
    os.system('clear')

print("berhasil")

# Koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbpersediaan"
)

if db.is_connected():
    print("berhasil")

mycursor = db.cursor()
lagi = "Y"

while lagi.upper() != "T":
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

    mycenter(2, "Transaksi Pembelian Barang")
    gotoxy(13, 4, "No. Faktur : ")
    gotoxy(1, 5, "Tgl. Faktur[yyyy-mm-dd] : ")
    gotoxy(60, 4, "Kode. Suplier : ")
    gotoxy(60, 5, "Nama. Suplier : ")

    ketemu = True
    while ketemu:
        nofak = myinput(27, 4, "")
        sql = "select * from tblbeli where nofak = %s"
        mycursor.execute(sql, (nofak,))
        myresult = mycursor.fetchone()
        if myresult is not None:
            pesan = "Nomor Faktur sudah digunakan.."
            gotoxy(27, 4, pesan)
            input()
            gotoxy(27, 4, " " * len(pesan))
        else:
            ketemu = False
            tglfak = myinput(27, 5, "")

    ketemu = False
    while not ketemu:
        kdsup = myinput(76, 4, "")
        sql = "Select * from tblsuplier where kodesup = %s"
        mycursor.execute(sql, (kdsup,))
        myresult = mycursor.fetchone()
        if myresult is None:
            pesan = "Suplier tidak di temukan.. "
            gotoxy(76, 4, pesan)
            input()
            gotoxy(76, 4, " " * len(pesan))
        else:
            ketemu = True
            nmsup = myresult[1]
            gotoxy(76, 5, nmsup)

            hline = "-" * 95
            gotoxy(1, 6, hline)
            gotoxy(5, 7, "  No  Kode        Nama        Stok        Harga      Jumlah      Total")
            gotoxy(5, 8, "      Barang      Barang      Barang      Beli       Beli        Harga ")
            gotoxy(1, 9, hline)

            no = 1
            brs = 10
            totitem = 0
            totbayar = 0
            kdbrg = "tidak kosong"
            while kdbrg != "":
                gotoxy(5, brs, str(no))
                kdbrg = myinput(10, brs, "")

                if kdbrg == "":
                    break
                sql = "Select * from tblbarang where kd_barang = %s"
                mycursor.execute(sql, (kdbrg,))
                databrg = mycursor.fetchone()

                if databrg is None:
                    pesan = "kode %s Tidak Ditemukan " % kdbrg
                    gotoxy(5, brs + 1, pesan)
                    input()
                    gotoxy(5, brs + 1, " " * len(pesan))
                else:
                    nmbrg = databrg[1]
                    stok = databrg[4]

                    gotoxy(20, brs, nmbrg)
                    gotoxy(34, brs, str(stok))
                    hrgbeli = int(myinput(40, brs, ""))
                    gotoxy(40, brs, "{:12n}".format(hrgbeli))
                    jmlbeli = int(myinput(55, brs, ""))
                    gotoxy(55, brs, "{:6n}".format(jmlbeli))

                    tothrg = hrgbeli * jmlbeli
                    gotoxy(66, brs, "{:12n}".format(tothrg))

                    no += 1
                    brs += 1

                    # Simpan ke tabel detail beli
                    sql = "INSERT INTO tbldetailbeli (nofak, kd_barang, jml) VALUES (%s, %s, %s)"
                    val = (nofak, kdbrg, jmlbeli)
                    mycursor.execute(sql, val)
                    db.commit()

                    # Update data stok di tabel barang
                    sql = "UPDATE tblbarang SET stok = %s WHERE kd_barang = %s"
                    val = (stok + jmlbeli, kdbrg)
                    mycursor.execute(sql, val)
                    db.commit()

                    totitem += jmlbeli
                    totbayar += tothrg

            # Simpan ke tabel beli
            sql = "INSERT INTO tblbeli (nofak, tanggal, kodesup, totalitem, totalbayar) VALUES (%s, %s, %s, %s, %s)"
            val = (nofak, tglfak, kdsup, totitem, totbayar)
            mycursor.execute(sql, val)
            db.commit()

            gotoxy(1, brs, hline)  # Cetak garis datar
            gotoxy(55, brs + 1, "{:6n}".format(totitem))
            gotoxy(66, brs + 1, "{:12n}".format(totbayar))
            gotoxy(1, brs + 2, hline)  # Cetak garis datar

            lagi = myinput(5, brs + 3, "Ada Faktur lagi (y/T]: ")
