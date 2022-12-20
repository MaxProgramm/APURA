from old import entry

rawDataFile = open("../rawData.txt")
outFile = open("../output.txt", "a")

test = entry.pInRoomLister(rawDataFile)
print (test)

counter = 0
for EntryPoint in test:
    a = test[counter]
    b = test[counter + 1]
    for line in rawDataFile:
        ep = entry.entryPointConstructer(line)
        if ep.pos > a.pos:
            ep.pInRoom = True
            outFile.write(ep.logEntryPointBuilder())

rawDataFile.close()
outFile.close()