
mulai = 100
akhir = 500

kelipatan_3_dan_5 = [x for x in range(mulai, akhir + 1) if x % 3 == 0 and x % 5 == 0]

jumlah = len(kelipatan_3_dan_5)

print("Bilangan kelipatan 3 dan 5 antara 100 dan 500:")
print(kelipatan_3_dan_5)
print("\nJumlah bilangan kelipatan 3 dan 5:", jumlah)
