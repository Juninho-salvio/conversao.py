# Escreva um programa que leia um valor em
# metros e o exiba
# convertido em centimentros e milimetros
n1 = float(input('Escreva o valor em metros: '))
c = n1 * 100
m = n1 * 1000
print('Quantos metros:      {}' .format(n1))
print('Quantos centimetros: {}' .format(c))
print('Quantos milimetros:  {}' .format(m))
#km, hm,dam,m,dm,cm,mm
km = n1 * 0.001
hm = n1 * 0.01
dam = n1 * 0.1
dm = n1 * 10
print('Qnatos km:           \033[4;31m{}\033[m' .format(km))
print('quantos hm:          \033[4;33m{}\033[m' .format(hm))
print('Quantos dam:         \033[4;32m{:.1f}\033[m' .format(dam))
print('Quantos dm:          \033[4;36m{}' .format(dm))
