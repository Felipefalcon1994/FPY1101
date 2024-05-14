#Calculo de impuestos para declaración de renta

#Variables
renta = int(input("Ingrese su renta"))
if renta < 550000:
    renta * 0.05 
    print("SU TIPO IMPOSITIVO ES DEL 5%")
if renta >= 551000 and renta < 860000:
    renta * 0.15
    print("SU TIPO IMPOSITIVO ES DEL 15%")
if renta >= 860000 and renta < 935000:
    renta * 0.20
    print("SU TIPO IMPOSITIVO ES DEL 20%")
if renta >= 953000 and renta < 1305000:
    renta * 0.30
    print("SU TIPO IMPOSITIVO ES DEL 30%")
if renta >= 1305000:
    renta * 0.45         
    print("SU TIPO IMPOSITIVO ES DEL 45%")
