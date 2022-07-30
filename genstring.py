def addQuote(text):
    modText = f"\"{text}\""
    modText = modText.replace("\n", "").strip()
    return modText

with open("string.txt", "r") as file:
    lines = file.readlines()
    with open("Localizable.string", "w") as output:
        for eachLine in lines:
            split = list(map(addQuote, eachLine.split("\t", 1)))
            output.write(f"{split[0]} = {split[1]};\n")