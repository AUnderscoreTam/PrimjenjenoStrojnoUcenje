listaBrojeva = [0]

i =0
i2 =0

while(listaBrojeva[i] != "done"):
    listaBrojeva.append((input()))
    i+=1
print("yippe")

listaBrojeva.pop()
listaBrojeva.pop(0)

while(i2 < i-1):
    listaBrojeva[i2] = int(listaBrojeva[i2])
    i2+=1

print(i-1)
print(min(listaBrojeva))
print(max(listaBrojeva))
print(sum(listaBrojeva)/i-1)
listaBrojeva.sort

print(listaBrojeva)



