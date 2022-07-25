nama = input("Nama : ")
nim = input("Nim : ")
prodi = input("Prodi : ")

def total_nilai (absen, tugas, uts, uas) :
    absen = int(absen) * 0.1
    tugas = int(tugas) * 0.2
    uts = int(uts) * 0.3
    uas = int(uas) * 0.4
    nilai_akhir = absen + tugas + uts + uas
    return nilai_akhir


def n (nilai) :
    a = ""
    if (nilai >= 0 and nilai < 31) :
        a = "D"
    elif (nilai >= 31 and nilai < 61) :
        a = "C"
    elif (nilai >= 61 and nilai < 81) :
        a = "B" 
    elif (nilai >= 81 and nilai < 100) :
        a = "A"
    return a

def e (h) :
    p = ""
    if (h >= 0 and h < 60) :
        p = "Tidak Lulus"
    elif (h >= 61 and h < 100) :
        p = "Lulus" 
    return p
    
def b () :
    hasil = 0
    for i in range (1,2) :
        print ("........Nilai Ke", i, ".........")
        nilai_absen = input("nilai_absen : ")
        nilai_tugas = input("nilai_tugas : ")
        nilai_uts = input("nilai_uts : ")
        nilai_uas = input("nilai_uas : ")
        hasil += (int(total_nilai(nilai_absen, nilai_tugas, nilai_uts, nilai_uas)))
    return hasil / i

total = b ()

print("........Total Nilai........")
print("Total nilai akhir yang didapat : ", total)

print("Nilai akhir yang didapat : ", n (total))
print("Keterangan : ", e (total))
    
