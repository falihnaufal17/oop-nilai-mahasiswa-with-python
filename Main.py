# Define class mahasiswa
from Mahasiswa import Mahasiswa

def main():
    # Define empty array
    list = []

    # Set count from zero
    count = 0

    x = input("Masukan Jumlah Mahasiswa: ")
    print("\n")

    # while count less than x, e.g: 0 < 2
    # it will display input
    # after that, append object Mahasiswa into array list
    while (count < int(x)):
        count += 1
        print("================================")
        print("Mahasiswa ke: " + str(count))
        print("================================ \n\n")

        nama = input("Masukan Nama Mahasiswa: ")
        n_absen = input("Masukan Nilai Absen: ")
        n_tugas = input("Masukan Nilai Tugas: ")
        n_uts = input("Masukan Nilai UTS: ")
        n_uas = input("Masukan Nulai UAS: ")

        # Set value object to class Mahasiswa
        list.append(Mahasiswa(nama, int(n_absen), int(n_tugas), int(n_uts), int(n_uas)))
        print("\n")

    # mapping all data from list
    for obj in list:
        Mahasiswa.calculateNilai(obj)
        Mahasiswa.calculateAverege(obj)
        Mahasiswa.generateGrade(obj)

        print(obj.nama, obj.n_absen, obj.n_tugas, obj.n_uts, obj.n_uas, obj.nilaiAkhir, obj.averege, obj.grade, sep= ' ')
main()