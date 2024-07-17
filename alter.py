import psycopg2

try:
    # Membuat koneksi ke database PostgreSQL
    conn = psycopg2.connect(
        dbname="testing",
        user="postgres",
        password="12345678",
        host="127.0.0.1",
        port="5432"
    )
    cursor = conn.cursor()
    
    # Mengubah tipe data kolom dari CHAR ke TEXT
    cursor.execute('''
        ALTER TABLE tb1
        ALTER COLUMN barang
        TYPE TEXT
    ''')
    
    # Menyimpan perubahan
    conn.commit()
    
    print("Tipe data kolom berhasil diubah!")
    
    # Menutup cursor dan koneksi
    cursor.close()
    conn.close()
except Exception as e:
    print("Terjadi kesalahan:", e)
