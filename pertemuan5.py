# Membuat Fungsi untuk mengkonversi suhu
def Konversi_Suhu(Temperature, value):
    if value == 'C':
        Temperatur_suhu = (Temperature - 32) * 5/9
        return Temperatur_suhu, 'C'
    else:
        Temperatur_suhu = (Temperature * 9/5) + 32
        return Temperatur_suhu, 'F'
    
    # Konversi dari Celsius ke Fahrenheit
celsius_temperatur = 30
Temperatur_suhu, target_value = Konversi_Suhu(celsius_temperatur, 'F')
print(f"{celsius_temperatur}°C dikonversi ke Fahrenheit adalah {Temperatur_suhu}°{target_value}")
