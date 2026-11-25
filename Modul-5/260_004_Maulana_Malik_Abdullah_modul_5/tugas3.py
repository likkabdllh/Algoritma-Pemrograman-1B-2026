def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = tugas * 0.30 + uts * 0.30 + uas * 0.40

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("\n=== HASIL NILAI MAHASISWA ===")
    print("Nama        :", nama)
    print("Nilai Akhir :", round(nilai_akhir, 2))
    print("Grade       :", grade)
    print("Status      :", status)

nama = input("Masukkan nama mahasiswa: ")
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

hitung_nilai(nama, tugas, uts, uas)
