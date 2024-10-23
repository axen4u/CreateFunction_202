# Membuat Fungsi untuk mengkonversi suhu
def Konversi_Suhu(Temperature, value):
    if value == 'C':
        Temperatur_suhu = (Temperature - 32) * 5/9
        return Temperatur_suhu, 'C'
    else:
        Temperatur_suhu = (Temperature * 9/5) + 32
        return Temperatur_suhu, 'F'