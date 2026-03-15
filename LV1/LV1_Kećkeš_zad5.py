separatedWords = []
dic = {}
fileHandler = open("song.txt")
for line in fileHandler:
    separatedWords = (line.split())
    for word in separatedWords:
        wordFilterd = word.removesuffix(",")
        wordFilterd = wordFilterd.lower()
        if wordFilterd in dic:
            dic[wordFilterd] += 1
        else:
            dic[wordFilterd] = 1


print(dic)
