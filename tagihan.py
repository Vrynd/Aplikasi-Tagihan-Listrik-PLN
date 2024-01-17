import os
from koneksi import Connection
from pelanggan import cari_Pelanggan
conn = Connection()
cursor = conn.cursor()

def tagihan_Pelanggan():
    count = 0
    while True:
        pelanggan_id = input("Masukan Id Pelanggan : ")
        cursor.execute("SELECT * FROM pelanggan WHERE id = %s", (pelanggan_id,))
        pelanggan = cursor.fetchone()
        if pelanggan == None:
            print(f"Pelanggan Dengan ID {pelanggan_id} Tidak Ditemukan")
        else:
            tanggal_bayar = input("Masukan Tanggal Bayar [Contoh: 2024-01-16] : ")
            beban_penggunaan = int(input("Masukan Beban Penggunaan [Contoh: 100]: "))
            bulan_tahun = input("Masukan Bulan & Tahun [Contoh: JAN/2024] : ")
            tagihan = beban_penggunaan * pelanggan[3]
            sql = "INSERT INTO tagihan(pelanggan_id, tanggal_bayar, beban_penggunaan, tagihan, bulan_tahun, status) VALUES(%s, %s, %s, %s, %s, 1)"
            data = (pelanggan_id, tanggal_bayar, beban_penggunaan, tagihan, bulan_tahun)
            cursor.execute(sql,data)
            conn.commit()
            count += 1
            # Konfirmasi jika ingin menambah tagihan pelanggan lagi
            os.system('cls')
            lagi = input("Apakah Ingin Menambah Tagihan Pelanggan Lagi ? [Y/T] : ")
            if lagi != "y" and lagi != 'Y':
                print("{} Tagihan Berhasil Ditambahkan".format(count), "\n")
                break

def tampilkanStruk():
    pelanggan_id = input("Masukan Id Pelanggan : ")
    pelanggan = cari_Pelanggan(pelanggan_id)
    if pelanggan == None:
        print(f"Pelanggan Dengan ID {pelanggan_id} Tidak Ditemukan!")
    else:
        cursor.execute("SELECT * FROM tagihan WHERE pelanggan_id=%s ORDER BY tanggal_bayar DESC LIMIT 1", (pelanggan_id,))
        tagihan = cursor.fetchone()
        if tagihan is None:
            print(f"Tagihan Pelanggan Dengan ID {pelanggan_id} Tidak Ditemukan!")
        else:
            tanggal, resi, pelanggan_id, nama_pelanggan, tarif, daya, beban, tagihan, bulan_tahun = tagihan[2], tagihan[0], pelanggan_id, pelanggan[1], pelanggan[2], pelanggan[3], tagihan[3], tagihan[4], tagihan[5]
            print("="*40)
            print("         STRUK PEMBAYARAN LISTRIK        ")
            print(f"Tanggal     : {tanggal}")
            print(f"No.Resi     : {resi}")
            print("-"*40)
            print(f"ID Pelanggan      : {pelanggan_id}")
            print(f"Nama Pelanggan    : {nama_pelanggan}")
            print(f"Tarif/Daya        : {tarif}/{daya}")
            print(f"Beban             : {beban}")
            print(f"Tagihan PLN Rp.   : {tagihan}")
            print(f"Bulan/Tahun       : {bulan_tahun}")
            print("="*40,"\n")
