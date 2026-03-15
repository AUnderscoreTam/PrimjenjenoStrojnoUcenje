FileName = input()
a = 0
b = []
sum = 0
result = 0
FileHandle = open(FileName)
for line in FileHandle:
    if (line.__contains__("X-DSPAM-Confidence:")):
        a += 1
        temp = line.removesuffix("\n")
        b.append(float(temp.removeprefix("X-DSPAM-Confidence: ")))

for i in b:
    sum += i

result = sum/a
print(result)
