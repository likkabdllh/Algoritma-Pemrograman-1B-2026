# SISTEM PENYEWAAN KENDARAAN BERMOTOR

kendaraan = [
    {"kode": "M01", "nama": "Honda Beat", "jenis": "Motor", "harga": 75000, "status": "Tersedia"},
    {"kode": "M02", "nama": "Honda Vario", "jenis": "Motor", "harga": 90000, "status": "Tersedia"},
    {"kode": "M03", "nama": "Yamaha NMAX", "jenis": "Motor", "harga": 120000, "status": "Tersedia"},
    {"kode": "M04", "nama": "Honda PCX", "jenis": "Motor", "harga": 130000, "status": "Tersedia"},
    {"kode": "M05", "nama": "Yamaha Aerox", "jenis": "Motor", "harga": 110000, "status": "Tersedia"},
    {"kode": "K01", "nama": "Toyota Avanza", "jenis": "Mobil", "harga": 350000, "status": "Tersedia"},
    {"kode": "K02", "nama": "Honda Brio", "jenis": "Mobil", "harga": 300000, "status": "Tersedia"},
    {"kode": "K03", "nama": "Toyota Innova", "jenis": "Mobil", "harga": 500000, "status": "Tersedia"},
    {"kode": "K04", "nama": "Mitsubishi Xpander", "jenis": "Mobil", "harga": 450000, "status": "Tersedia"},
    {"kode": "K05", "nama": "Toyota Calya", "jenis": "Mobil", "harga": 280000, "status": "Tersedia"}
]

jenis_kendaraan = ("Motor", "Mobil")
transaksi = {}
akun_admin = {"admin01": "12345", "admin02": "67890", "admin03": "adminku"}
akun_user = {}


def cari_kendaraan(kode):
    for k in kendaraan:
        if k["kode"] == kode.upper():
            return k
    return None


def tampilkan_kendaraan():
    print("\n========== DAFTAR KENDARAAN ==========")
    for jenis in jenis_kendaraan:
        print(f"\n--- {jenis.upper()} ---")
        for k in kendaraan:
            if k["jenis"] == jenis:
                print(f'{k["kode"]} | {k["nama"]} | Rp{k["harga"]:,}/hari | {k["status"]}')

    input("\nTekan Enter untuk kembali ke menu...")
def input_angka(pesan):
    try:
        return int(input(pesan))
    except ValueError:
        print("Input harus berupa angka!")
        return 0


def sewa_kendaraan(nama):
    tampilkan_kendaraan()
    k = cari_kendaraan(input("\nMasukkan kode kendaraan: "))

    if not k:
        print("Kode kendaraan tidak ditemukan!")
        return

    if k["status"] == "Disewa":
        print("Maaf, kendaraan sedang disewa!")
        return

    lama = input_angka("Lama penyewaan (hari): ")
    if lama <= 0:
        print("Lama penyewaan harus lebih dari 0!")
        return

    total = k["harga"] * lama

    print("\n========== DETAIL PENYEWAAN ==========")
    print("Nama Penyewa :", nama)
    print("Kendaraan    :", k["nama"])
    print("Harga/Hari   : Rp", format(k["harga"], ","))
    print("Lama Sewa    :", lama, "hari")
    print("Total Bayar  : Rp", format(total, ","))

    if input("\nLanjutkan penyewaan? (y/n): ").lower() == "y":
        id_sewa = "TR" + str(len(transaksi) + 1)

        transaksi[id_sewa] = {
            "nama": nama,
            "kode": k["kode"],
            "kendaraan": k["nama"],
            "lama": lama,
            "total": total,
            "status": "Sedang Disewa"
        }

        k["status"] = "Disewa"
        print("\nPenyewaan berhasil!")
        print("ID Transaksi:", id_sewa)
    else:
        print("Penyewaan dibatalkan.")


def riwayat_user(nama):
    print("\n========== RIWAYAT PENYEWAAN ==========")
    ditemukan = False

    for id_sewa, data in transaksi.items():
        if data["nama"].lower() == nama.lower():
            ditemukan = True
            print(f"\nID Transaksi : {id_sewa}")
            print("Kendaraan    :", data["kendaraan"])
            print("Lama Sewa    :", data["lama"], "hari")
            print("Total Bayar  : Rp", format(data["total"], ","))
            print("Status       :", data["status"])

    if not ditemukan:
        print("Kamu belum memiliki transaksi.")
    input("\nTekan Enter untuk kembali ke menu...")

def ajukan_pengembalian(nama):
    id_sewa = input("\nMasukkan ID Transaksi: ").upper()

    if id_sewa not in transaksi:
        print("ID transaksi tidak ditemukan!")
        return

    data = transaksi[id_sewa]

    if data["nama"].lower() != nama.lower():
        print("Transaksi tersebut bukan milik kamu!")
        return

    if data["status"] != "Sedang Disewa":
        print("Transaksi tidak dapat diajukan!")
        return

    data["status"] = "Menunggu Konfirmasi Pengembalian"
    print("\nPengajuan pengembalian berhasil!")
    print("Silakan tunggu konfirmasi dari admin.")


def tambah_kendaraan():
    kode = input("\nMasukkan kode kendaraan: ").upper()

    if cari_kendaraan(kode):
        print("Kode kendaraan sudah digunakan!")
        return

    nama = input("Masukkan nama kendaraan: ")
    jenis = input("Masukkan jenis kendaraan (Motor/Mobil): ").capitalize()
    harga = input_angka("Masukkan harga sewa per hari: ")

    if jenis not in jenis_kendaraan or harga <= 0:
        print("Jenis atau harga tidak valid!")
        return

    kendaraan.append({
        "kode": kode,
        "nama": nama,
        "jenis": jenis,
        "harga": harga,
        "status": "Tersedia"
    })

    print("\nKendaraan berhasil ditambahkan!")


def edit_kendaraan():
    tampilkan_kendaraan()
    k = cari_kendaraan(input("\nMasukkan kode kendaraan yang ingin diedit: "))

    if not k:
        print("Kode kendaraan tidak ditemukan!")
        return

    if k["status"] == "Disewa":
        print("Kendaraan sedang disewa, tidak dapat diedit!")
        return

    print("\nKosongkan input jika data tidak ingin diubah.")

    nama = input("Nama baru: ").strip()
    jenis = input("Jenis baru (Motor/Mobil): ").strip().capitalize()
    harga = input("Harga baru per hari: ").strip()

    if nama:
        k["nama"] = nama

    if jenis:
        if jenis not in jenis_kendaraan:
            print("Jenis kendaraan tidak valid!")
            return
        k["jenis"] = jenis

    if harga:
        harga = int(harga) if harga.isdigit() else 0
        if harga <= 0:
            print("Harga harus lebih dari 0!")
            return
        k["harga"] = harga

    print("\nData kendaraan berhasil diperbarui!")


def hapus_kendaraan():
    tampilkan_kendaraan()
    k = cari_kendaraan(input("\nMasukkan kode kendaraan yang ingin dihapus: "))

    if not k:
        print("Kode kendaraan tidak ditemukan!")
        return

    if k["status"] == "Disewa":
        print("Kendaraan sedang disewa, tidak dapat dihapus!")
        return

    if input(f"Yakin ingin menghapus {k['nama']}? (y/n): ").lower() == "y":
        kendaraan.remove(k)
        print("\nKendaraan berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan!")


def semua_transaksi():
    print("\n========== SELURUH DATA PENYEWAAN ==========")

    if not transaksi:
        print("Belum ada transaksi penyewaan.")
        return

    for id_sewa, data in transaksi.items():
        print(f"\nID Transaksi : {id_sewa}")
        print("Nama         :", data["nama"])
        print("Kendaraan    :", data["kendaraan"])
        print("Kode         :", data["kode"])
        print("Lama Sewa    :", data["lama"], "hari")
        print("Total Bayar  : Rp", format(data["total"], ","))
        print("Status       :", data["status"])


def konfirmasi_pengembalian():
    print("\n========== KONFIRMASI PENGEMBALIAN ==========")
    pengajuan = {
        id: data for id, data in transaksi.items()
        if data["status"] == "Menunggu Konfirmasi Pengembalian"
    }

    if not pengajuan:
        print("Tidak ada pengajuan pengembalian.")
        return

    for id_sewa, data in pengajuan.items():
        print(f"\nID Transaksi : {id_sewa}")
        print("Nama         :", data["nama"])
        print("Kendaraan    :", data["kendaraan"])

    id_sewa = input("\nMasukkan ID Transaksi: ").upper()

    if id_sewa not in pengajuan:
        print("Transaksi tidak ditemukan atau belum menunggu konfirmasi!")
        return

    transaksi[id_sewa]["status"] = "Sudah Dikembalikan"

    for k in kendaraan:
        if k["kode"] == transaksi[id_sewa]["kode"]:
            k["status"] = "Tersedia"
            break

    print("\nPengembalian berhasil dikonfirmasi!")


def total_pendapatan():
    total = sum(data["total"] for data in transaksi.values())

    print("\n========== LAPORAN PENDAPATAN ==========")
    print("Jumlah Transaksi :", len(transaksi))
    print("Total Pendapatan : Rp", format(total, ","))


def statistik_kendaraan():
    tersedia = sum(k["status"] == "Tersedia" for k in kendaraan)
    disewa = sum(k["status"] == "Disewa" for k in kendaraan)

    print("\n========== STATISTIK KENDARAAN ==========")
    print("Total Kendaraan    :", len(kendaraan))
    print("Kendaraan Tersedia :", tersedia)
    print("Kendaraan Disewa   :", disewa)


def tambah_admin():
    username = input("\nBuat username admin baru: ").strip()
    password = input("Buat password: ").strip()

    if not username or not password:
        print("Username dan password tidak boleh kosong!")
        return

    if username in akun_admin or username in akun_user:
        print("Username sudah digunakan!")
        return

    akun_admin[username] = password
    print("\nAkun admin berhasil dibuat!")
    print("Username:", username)


def daftar_admin():
    print("\n========== DAFTAR AKUN ADMIN ==========")
    for username in akun_admin:
        print("-", username)


def hapus_akun_user(nama):
    print("\n========== HAPUS AKUN USER ==========")
    if nama not in akun_user:
        print("Akun User tidak ditemukan!")
        return False

    if input("Yakin ingin menghapus akun kamu? (y/n): ").lower() == "y":
        del akun_user[nama]
        print("Akun User berhasil dihapus. Kamu akan logout.")
        return True

    print("Penghapusan akun dibatalkan.")
    return False


def hapus_akun_user_admin():
    print("\n========== HAPUS AKUN USER ==========")
    if not akun_user:
        print("Belum ada akun User yang terdaftar.")
        return

    print("Daftar akun User:")
    for username in akun_user:
        print("-", username)

    username = input("Masukkan username User yang ingin dihapus: ").strip()
    if username not in akun_user:
        print("Akun User tidak ditemukan!")
        return

    if input(f"Yakin ingin menghapus akun {username}? (y/n): ").lower() == "y":
        del akun_user[username]
        print("Akun User berhasil dihapus!")
    else:
        print("Penghapusan akun dibatalkan.")


def hapus_akun_admin_sendiri(username):
    print("\n========== HAPUS AKUN ADMIN SENDIRI ==========")
    if username not in akun_admin:
        print("Akun Admin tidak ditemukan!")
        return False

    if input("Yakin ingin menghapus akun Admin kamu sendiri? (y/n): ").lower() == "y":
        del akun_admin[username]
        print("Akun Admin berhasil dihapus. Kamu akan logout.")
        return True

    print("Penghapusan akun dibatalkan.")
    return False


def menu_user(nama):
    while True:
        print("\n========== MENU USER ==========")
        print("Nama:", nama)
        print("1. Daftar Kendaraan")
        print("2. Sewa Kendaraan")
        print("3. Riwayat Penyewaan")
        print("4. Ajukan Pengembalian")
        print("5. Hapus Akun Saya")
        print("6. Logout")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_kendaraan()
        elif pilihan == "2":
            sewa_kendaraan(nama)
        elif pilihan == "3":
            riwayat_user(nama)
        elif pilihan == "4":
            ajukan_pengembalian(nama)
        elif pilihan == "5":
            if hapus_akun_user(nama):
                break
        elif pilihan == "6":
            print("Berhasil logout!")
            break
        else:
            print("Pilihan tidak tersedia!")


def menu_admin(username):
    menu = {
        "1": tampilkan_kendaraan,
        "2": tambah_kendaraan,
        "3": edit_kendaraan,
        "4": hapus_kendaraan,
        "5": semua_transaksi,
        "6": konfirmasi_pengembalian,
        "7": total_pendapatan,
        "8": statistik_kendaraan,
        "9": tambah_admin,
        "10": daftar_admin,
        "11": hapus_akun_user_admin
    }

    while True:
        print("\n========== MENU ADMIN ==========")
        print("Admin:", username)
        print("1. Daftar Kendaraan")
        print("2. Tambah Kendaraan")
        print("3. Edit Kendaraan")
        print("4. Hapus Kendaraan")
        print("5. Seluruh Data Penyewaan")
        print("6. Konfirmasi Pengembalian")
        print("7. Total Pendapatan")
        print("8. Statistik Kendaraan")
        print("9. Tambah Akun Admin")
        print("10. Daftar Akun Admin")
        print("11. Hapus Akun User")
        print("12. Hapus Akun Admin Saya")
        print("13. Logout")

        pilihan = input("Pilih menu (1-13): ")

        if pilihan == "12":
            if hapus_akun_admin_sendiri(username):
                break
        elif pilihan == "13":
            print("Berhasil logout!")
            break
        elif pilihan in menu:
            menu[pilihan]()
        else:
            print("Pilihan tidak tersedia!")


def daftar_user():
    print("\n========== DAFTAR AKUN USER ==========")
    print("Ketentuan username: harus mengandung huruf. Angka boleh ditambahkan, tetapi tidak boleh hanya angka.")
    username = input("Buat username: ").strip()
    password = input("Buat password: ").strip()

    if not username or not password:
        print("Username dan password tidak boleh kosong!")
        return

    if not username.isalnum() or not any(huruf.isalpha() for huruf in username):
        print("Username tidak valid! Username harus mengandung huruf dan tidak boleh hanya berupa angka atau memakai simbol.")
        return

    if username in akun_admin or username in akun_user:
        print("Username sudah digunakan! Silakan gunakan username lain.")
        return

    akun_user[username] = password
    print("\nAkun User berhasil dibuat!")
    print("Sekarang kamu bisa login menggunakan akun tersebut.")


def login():
    print("\n========== LOGIN ==========")
    username = input("Username: ").strip()
    password = input("Password: ")

    # Periksa akun Admin terlebih dahulu
    if akun_admin.get(username) == password:
        print("\nLogin berhasil sebagai Admin!")
        print("Selamat datang,", username)
        menu_admin(username)

    # Jika bukan Admin, periksa akun User
    elif akun_user.get(username) == password:
        print("\nLogin berhasil sebagai User!")
        print("Selamat datang,", username)
        menu_user(username)

    # Username terdaftar tetapi password salah
    elif username in akun_admin or username in akun_user:
        print("\nPassword salah!")

    # Username belum terdaftar
    else:
        print("\nAkun belum terdaftar!")
        print("Silakan tambahkan/daftarkan akun terlebih dahulu melalui menu Daftar Akun User.")


def program_utama():
    while True:
        print("\n========== SISTEM PENYEWAAN KENDARAAN ==========")
        print("1. Login")
        print("2. Daftar Akun User")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            login()

        elif pilihan == "2":
            daftar_user()

        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan program!")
            break

        else:
            print("Pilihan tidak tersedia!")

program_utama()