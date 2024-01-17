import os
from koneksi import Connection
conn = Connection()
cursor = conn.cursor()

def tambah_Pelanggan():
    count = 0
    while True :
        id = input("Massukan Id Pelangan : ")
        pelanggan = cari_Pelanggan(id)
        if pelanggan != None:
            print(f"*Pelanggan Dengan ID {id} Sudah Ada\n")
        else:
            nama_pelanggan = input("Massukan Nama Pelanggan : ")
            tarif_daya = input("Massukan Tarif Daya : ")
            tarif_watt = input("Massukan Tarif Watt : ")
            sql = "INSERT INTO pelanggan(id, nama_pelanggan, tarif_daya, tarif_watt) VALUES (%s, %s, %s, %s)"
            val = (id, nama_pelanggan, tarif_daya, tarif_watt)
            cursor.execute(sql,val)
            conn.commit()
            count += 1
            # Konfirmasi jika ingin menambah pelanggan lagi
            os.system('cls')
            lagi = input("Apakah Ingin Menambah Pelanggan Lagi ? [Y/T] : ")
            if lagi != "y" and lagi != 'Y':
                print("{} Data Berhasil Ditambahkan".format(count), "\n")
                break

def ubah_Pelanggan():
    count = 0
    while True:
        tampilkan_Pelanggan()
        id = input("Massukan Id Pelanggan Yang Ingin Dirubah : ")
        pelanggan = cari_Pelanggan(id)
        if pelanggan == None:
            print(f"*Pelanggan Dengan ID {id} Tidak Ada\n")
        else:
            cursor.execute("SELECT * FROM pelanggan WHERE id="+id)
            result = cursor.fetchall()
            for data in result:
                nama_pelanggan = input("Nama Pelanggan : "+data[1]+ " -> ") or data[1]
                tarif_daya = input("Tarif Daya : "+data[2]+ " -> ") or data[2]
                tarif_watt = input("Tarif Watt : "+str(data[1])+ " -> ") or str(data[3])
            sql = "UPDATE pelanggan SET nama_pelanggan=%s, tarif_daya=%s, tarif_watt=%s WHERE id=%s"
            val = (nama_pelanggan, tarif_daya, tarif_watt, id)
            cursor.execute(sql, val)
            conn.commit()
            count += 1
            # Konfirmasi jika ingin mengubah pelanggan lagi
            os.system('cls')
            lagi = input("Apakah Ingin Mengubah Pelanggan Lagi ? [Y/T] : ")
            if lagi != "y" and lagi != 'Y':
                print("{} Data Berhasil Diubah".format(count),"\n")
                break

def hapus_Pelanggan():
    count = 0
    while True:
        tampilkan_Pelanggan()
        id = input("Massukan Id yang ingin dihapus : ")
        pelanggan = cari_Pelanggan(id)
        if pelanggan == None:
            print(f"*Pelanggan Dengan ID {id} Tidak Ada\n")
        else:
            # Konfirmasi yakin ingin menghapus data ini
            yakin = input("Apakah Yakin Menghapus Data Ini [Y/T] : ")
            if yakin == 'y' or yakin =='Y':
                sql = "DELETE FROM pelanggan WHERE id=%s"
                val = (id,)
                cursor.execute(sql, val)
                conn.commit()
            count += 1
            # Konfirmasi jika ingin menghapus pelanggan lagi
            os.system('cls')
            lagi = input("Apakah Ingin Menghapus Pelanggan Lagi [Y/T] : ")
            if lagi != 'y' and lagi != 'Y':
                print("{} Data Berhasil Dihapus".format(count), "\n")

def cari_Pelanggan(id):
    sql = "SELECT * FROM pelanggan WHERE id=%s"
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    return result

def tampilkan_Pelanggan():
    sql = "SELECT * FROM pelanggan"
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) > 0:
        print("="*65)
        print("{:<10}{:<20}{:<20}{:<20}".format("Id", "Nama Pelanggan", "Tarif Daya", "Tarif Watt"))
        print("-"*65)
        for value in result:
            print("{:<10}{:<20}{:<20}{:>10}".format(value[0], value[1], value[2], value[3]))
        print("\n")
    elif len(result) == 0:
        print("Data Pelanggan Tidak Tersedia!\n")