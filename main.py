import os
from koneksi import Connection
from pelanggan import tambah_Pelanggan, ubah_Pelanggan, hapus_Pelanggan, tampilkan_Pelanggan
from tagihan import tagihan_Pelanggan, tampilkanStruk
conn = Connection()

def program_utama():
    while True:
        os.system("cls")
        print("1. Manajemen Pelanggan")
        print("2. Manajemen Tagihan")
        print("0. Keluar")
        menu = input(">> Masukan operasi [1/2/0] :")
        os.system("cls")
        if menu == "1":
            while True:
                print("1. Tambah Pelanggan")
                print("2. Ubah Pelanggan")
                print("3. Hapus Pelanggan")
                print("4. Tampilkan Pelanggan")
                print("0. Kembali Ke Menu")
                menu = input(">> Masukan Pilihan Menu [1/2/3/4/0] : ")
                os.system("cls")
                if menu == "1":
                    tambah_Pelanggan()
                elif menu == "2":
                    ubah_Pelanggan()
                elif menu == "3":
                    hapus_Pelanggan()
                elif menu == "4":
                    tampilkan_Pelanggan()
                elif menu == "0":
                    break
                else:
                    os.system("cls")
                    coba_lagi = input("*Pilihan Tidak Valid, Pilih Menu Lagi [Y/T] : ")
                    if coba_lagi == 't' or coba_lagi == 'T':
                        break
        elif menu == "2":
            while True:
                print("1. Tambah Tagihan")
                print("2. Cetak Struk")
                print("0. Kembali Ke Menu")
                menu = input(">> Masukan Pilihan Menu [1/2/0] : ")
                os.system('cls')
                if menu == "1":
                    tagihan_Pelanggan()
                elif menu == "2":
                    tampilkanStruk()
                elif menu == "0":
                    break
                else:
                    os.system("cls")
                    coba_lagi = input("*Pilihan Tidak Valid, Pilih Menu Lagi [Y/T] : ")
                    if coba_lagi == 't' or coba_lagi == 'T':
                        break
        elif menu == "0":
            print(">> Anda Keluar Dari Menu, Program Selesai!")
            exit()
        else:
            os.system("cls")
            coba_lagi = input("*Pilihan Tidak Valid, Pilih Menu Lagi [Y/T] : ")
            if coba_lagi == 't' or coba_lagi == 'T':
                break
program_utama()