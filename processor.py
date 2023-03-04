# takes the preRawData file as an input and pastes every line which does not contain "to" into the rawData file.
with open("preRawData.txt") as pre:
    with open("rawData.txt", "a") as past:
        for line in pre:
            if not line.__contains__("to"):
                past.write(line)