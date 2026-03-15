fileHandler = open("SMSSpamCollection.txt")

wordCount = {"ham": 0, "spam": 0}
numberOfAppearances = {"ham": 0, "spam": 0}
numberOfExlemetionMarks = 0

for line in fileHandler:

    if line.find("spam") >= 0:
        numberOfExlemetionMarks += line.count("!")

        numberOfAppearances["spam"] += 1
        for word in line.split():
            if word == "spam":
                continue
            wordCount["spam"] += 1

    elif line.find("ham") >= 0:
        numberOfAppearances["ham"] += 1

        for word in line.split():
            if word == "ham":
                continue
            wordCount["ham"] += 1

print("avarage word count human: ",
      wordCount["ham"] / numberOfAppearances["ham"])
print("avarage word count spam: ",
      wordCount["spam"] / numberOfAppearances["spam"])

print("number of exlemation marks: ", numberOfExlemetionMarks)
