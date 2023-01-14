from model.daftar_nilai import tambah_data, hapus_data, ubah_data

def input_data():
    while True:
        print(" ")
        print("===Input Data Mahasiswa===")
        nama = input('Nama Mahasiswa  : ')
        nim = int(input('NIM Mahasiswa   : '))
        tugas = int(input('Nilai Tugas     : '))
        nilaiUTS = int(input('Nilai UTS       : '))
        nilaiUAS = int(input('Nilai UAS       : '))
        nilaiAkhir = tugas * 30 / 100 + nilaiUTS * 35 / 100 + nilaiUAS * 35 / 100
        tambah_data(nama, nim, tugas, nilaiUTS, nilaiUAS, nilaiAkhir)
        tanya = input("Ingin tambah Data (y/n)?")
        if tanya.lower() == 'n':
            break

def hapuss():
    print(" ")
    print("Menu Hapus Data")
    hapus_data(input("Masukkan Data Yang Ingin Dihapus : "))

def cari_ubah():
    ubah_data(input("Masukkan Nama Yang Ingin Di ubah : "))

def ubahh():
    print(" ")
    print("===Masukkan Data Baru===")
    nama = input('Nama Mahasiswa  : ')
    nim = int(input('NIM Mahasiswa   : '))
    tugas = int(input('Nilai Tugas     : '))
    nilaiUTS = int(input('Nilai UTS       : '))
    nilaiUAS = int(input('Nilai UAS       : '))
    nilaiAkhir = tugas * 30 / 100 + nilaiUTS * 35 / 100 + nilaiUAS * 35 / 100
    tambah_data(nama, nim, tugas, nilaiUTS, nilaiUAS, nilaiAkhir)
    print("Data Berhasil diubah")
    kembali = input('Kembali Tekan [enter]')

def cari_data():
    from view.view_nilai import cetak_hasil_pencarian
    cetak_hasil_pencarian(input("Masukkan Nama yang ingin dicari : "))
