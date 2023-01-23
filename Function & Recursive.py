nama = " Aloysius Gonzaga Exalta Budisuryono"
nim = "\n 20210801020"
jrsn = "\n Teknik Informatika "
bio = nama + nim + jrsn
print (bio)

def tampilkanAngka (batas, i = 1):
  print(f'Perulangan ke {i}')

  if (i < batas):
    tampilkanAngka(batas, i + 1)

tampilkanAngka(5)
