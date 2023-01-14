while True:
    print("-------------Menu pilihan-------------")
    print("1. Tambah Data \n2. Ubah Data \n3. Hapus Data \n4. Cetak Data \n5. Cari Data \n6. Keluar")
    print(" ")
    inputt = input('Pilih Menu 1-6 :  ')
    if inputt == '1':
        from view.input_nilai import input_data
        input_data()
    elif inputt == '2':
        from view.input_nilai import cari_ubah
        cari_ubah()
    elif inputt == '3':
        from view.input_nilai import hapuss
        hapuss()
    elif inputt == '4':
        from view.view_nilai import tampilkan
        tampilkan()
    elif inputt == '5':
        from view.input_nilai import cari_data
        cari_data()
    elif inputt == '6':
        print("Terima Kasih telah menggunakan Program ini!")
        break
    else:
        print("Masukan Menu Pilihan dengan benar!")
