import psycopg2

try:
    # Membuat koneksi ke database PostgreSQL
    conn = psycopg2.connect(
        dbname="testing",
        user="postgres",  # Pastikan ini adalah user yang benar
        password="12345678",
        host="127.0.0.1",
        port="5432"
    )
    print("Koneksi berhasil!")
    
    # Membuat objek cursor
    cursor = conn.cursor()
    
    sql = "delete from tb1 WHERE id=%s"
    data = ("2")

    cursor.execute(sql, data)
    conn.commit()

    # Contoh menjalankan perintah SQL sederhana
    cursor.execute("SELECT * from tb1")
    db_version = cursor.fetchall()
    print(db_version)
    
    # Menutup cursor dan koneksi
    cursor.close()
    conn.close()
except Exception as e:
    print("Terjadi kesalahan:", e)
