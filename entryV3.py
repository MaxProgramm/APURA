# pos; temp; pInRoom; time
rawDataFile = "rawData.txt"
outputFile = "output.txt"
# IMPORTANT
pInRoomList = list()
movementSensorDeadTime = 5


class EntryPointCl:
    def __init__(self, pos, temp, pInRoom, time):
        self.pos = int(pos)
        self.temp = float(temp)
        self.pInRoom = bool(pInRoom)
        self.time = int(time)

    def logEntryPointBuilder(self):
        pInRoomString = bool
        if self.pInRoom:
            pInRoomString = "TRUE"
        else:
            pInRoomString = "FALSE"
        return f"{self.pos}; {self.temp}; {pInRoomString}; {self.time}"


def entryPointConstructer(line: str):
    pInRoom = False
    seperator = ";"
    pos = int(line.split(seperator)[0].replace(" ", ""))
    temp = float(line.split(seperator)[1].replace(" ", ""))
    if line.split(seperator)[2].replace(" ", "") == "TRUE":
        pInRoom = True
    elif line.split(seperator)[2].replace(" ", "") == "FALSE":
        pInRoom = False
    time = int(line.split(seperator)[3].replace(" ", ""))

    EntryPoint = EntryPointCl(pos, temp, pInRoom, time)
    return EntryPoint


def pInRoomLister(fileName = "rawData.txt"):
    with open(fileName) as file:
        for line in file:
            # DEBUG
            print(f"Current file and line of loader: {file.name} {line}")
            # IMPORTANT
            EntryPoint = entryPointConstructer(line)
            if EntryPoint.pInRoom:
                pInRoomList.append(EntryPoint)
        # DEBUG
        for i in pInRoomList:
            print(i.pos)
    return pInRoomList


def pInRoomFiller():
    print("pInRoomFiller was called")
    with open(rawDataFile) as file:
        for line in file:
            print("pInRoomFiller - first for loop")
            ep = entryPointConstructer(line)
            counter = 0
            found = False
            for x in pInRoomList:
                if pInRoomList.__len__() - 1 > counter:
                    a = pInRoomList[counter]
                    b = pInRoomList[counter + 1]
                    if a.pos < ep.pos < b.pos and b.time - a.time < movementSensorDeadTime:
                        ep.pInRoom = True
                        with open(outputFile, "a") as oF:
                            oF.write(ep.logEntryPointBuilder() + "\n")
                            found = True
                            break
                    counter = counter + 1
                else:
                    continue

            if found == False:
                with open(outputFile, "a") as oF:
                    oF.write(ep.logEntryPointBuilder() + "\n")


# entryPoint_A = entryPointConstructer("1; 28; TRUE; 32")

pInRoomLister()
pInRoomFiller()

print("test")
print("Finish! Entry")
