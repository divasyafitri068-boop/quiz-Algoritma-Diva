# Program Kelulusan Ujian Matematika

print("=====PROGRAM KELULUSAN MAHASISWA=====")
#input nama mahasiswa
Nama = input (" Masukkan Nama Mahasiswa: ")

#menentukan target nilai
if Nama == "Andi":
    target = 70
elif Nama == "Budi" :
    target = 75
elif Nama== "Citra" :
    target = 80
else:
    print("Nama Mahasiswa Tidak Terdaftar!")
    exit()

print("Nama Mahasiswa: ",Nama)
print("Target Nilai: ",target)

#perulangan ujian maksimal 3 kali
percobaan = 1
lulus = False

while percobaan <=3:
    nilai = int (input("Masukkan Nilai Ujian Ke-"+str(percobaan)+":"))
    
    if nilai>=target:
        lulus = True
        print("\nselamat,",Nama,"Berhasil Lulus!")
        print("Lulus Pada Percobaan Ke-",percobaan)
        break
    else:
        print("Nilai Belum Mencapai Target.")
        percobaan +=1
        
#hasil akhir
print("=====HASIL AKHIR=====")
if lulus==False:
    print("\nMaaf",Nama,"Tidak Lulus Setelah 3 Kali Percobaan.")