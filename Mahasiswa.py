class Mahasiswa:

    def __init__(self, nama, n_absen, n_tugas, n_uts, n_uas):
        self.nama = nama
        self.n_absen = n_absen
        self.n_tugas = n_tugas
        self.n_uts = n_uts
        self.n_uas = n_uas
        self.percentageAbsen = 0
        self.percentageTugas = 0
        self.percentageUts = 0
        self.percentageUas = 0
        self.nilaiAkhir = 0
        self.averege = 0
        self.grade = ''

    def calculateNilai(self):
        self.percentageAbsen = (self.n_absen / 100) * 10
        self.percentageTugas = (self.n_tugas / 100) * 20
        self.percentageUts = (self.n_uts / 100) * 30
        self.percentageUas = (self.n_uas / 100) * 40
        
        self.nilaiAkhir = self.percentageAbsen + self.percentageTugas + self.percentageUts + self.percentageUas
        float(self.nilaiAkhir)

        print("Nilai Akhir: " + str(self.nilaiAkhir))

    def calculateAverege(self):
        self.averege = ((self.percentageAbsen + self.percentageTugas + self.percentageUts + self.percentageUas) + float(self.nilaiAkhir)) / 2
        float(self.averege)

        print("Nilai Rata-rata: " + str(self.averege))

    def generateGrade(self):
        if (float(self.averege) >= 80):
            self.grade = 'A'
        elif (float(self.averege) >= 70 and float(self.averege) < 80):
            self.grade = 'B'
        elif (float(self.averege) >= 60 and float(self.averege) < 70):
            self.grade = 'C'
        elif (float(self.averege) >= 50 and float(self.averege) < 60):
            self.grade = 'D'
        else: 
            self.grade = 'E'

        print("Grade: " + self.grade)