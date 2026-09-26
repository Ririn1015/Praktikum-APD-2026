barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000

total_bayar = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
pajak = total_bayar * 0.15
total_bayar = total_bayar + pajak
rata_rata = total_bayar / 6
nim = 17
bolean = nim < rata_rata

print(barang_1)
print(barang_2)
print(barang_3)
print(barang_4)
print(barang_5)
print(barang_6)
print(total_bayar)
print(pajak)
print(rata_rata)
print(nim)
print(bolean)

barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]

kurs_usd = 16500
kurs_jpy = 110
total_usd = total_bayar / kurs_usd
total_jpy = total_bayar / kurs_jpy

barang_ganjil = barang[::2]
print(barang_ganjil)
print(total_usd)
print(total_jpy)