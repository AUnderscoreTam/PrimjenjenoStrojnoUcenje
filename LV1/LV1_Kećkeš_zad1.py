def total_euro(sati,placaPoSatu):
    return sati*placaPoSatu


sati = float(input())
print("Radni sati: ",sati)
placaPoSatu = float(input())
print("eura/h: ",placaPoSatu)

print("Ukupno: ",total_euro(sati,placaPoSatu)," eura")