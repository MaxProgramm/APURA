
class EntryPointCl:
    def __init__(self, pos, temp, pInRoom, time):
        self.pos = int(pos)
        self.temp = float(temp)
        self.pInRoom = bool(pInRoom)
        self.time = int(time)

    def logEntryPointBuilder(self):
        pInRoomString = bool
        if self.pInRoom == True:
            pInRoomString = "TRUE"
        else:
            pInRoomString = "FALSE"
        return (f"{self.pos}; {self.temp}; {pInRoomString}; {self.time}")

rawDataFile = open("../rawData.txt", "r")
outputFile = open("../output.txt", "a")
#IMPORTANT
global pInRoomList
pInRoomList = list()
movementSensorDeadTTime = 5



def entryPointConstructer(line = str):
    pInRoom = False
    seperator = ";"
    pos = int(line.split(seperator)[0].replace(" ", ""))
    temp = float(line.split(seperator)[1].replace(" ", ""))
    if line.split(seperator)[2].replace(" ", "") == "TRUE":
        pInRoom = True
    elif line.split(seperator)[2].replace(" ", "") == "FALSE":
        pInRoom = False
    # else:
    #     print("ERROR! entryPointConstructer - Person in Room Value bei Log Eintrag nicht WAHR oder FALSCH! Es muss aber entweder WAHR oder FALSCH sein!")
    time = int(line.split(seperator)[3].replace(" ", ""))

    EntryPoint = EntryPointCl(pos, temp, pInRoom, time)
    return EntryPoint

#EntryPoint = entryPointConstructer("1; 28; TRUE; 32")
#print(EntryPoint.time)

def pInRoomLister(file = rawDataFile):
    for line in file:
        # DEBUG
        print(f"Current file and line of loader: {file.name} {line}")
        #IMPORTANT
        EntryPoint = entryPointConstructer(line)
        if EntryPoint.pInRoom == True:
            pInRoomList.append(EntryPoint)
    # DEBUG
    for i in pInRoomList:
        print(i.pos)

    return pInRoomList

def entryPointLogConstructer(entryPoint):
    pos = entryPoint.pos
    time = entryPoint.time
    temp = entryPoint.temp
    if entryPoint.pInRoom:
        pInRoom = "TRUE"
    else:
        pInRoom = "FALSE"

    return (f"{pos}; {temp}; {pInRoom}; {time}")

def pInRoomFiller(inFile = rawDataFile, out = outputFile):
    counter = 0
    for i in pInRoomList:
        #print(i)
        a = pInRoomList[counter]
        b = pInRoomList[counter + 1]
        print(f"a: {a.pos} | b: {b.pos}")
        for x in inFile:
            print(str(x))
        counter = counter + 1
        #for line in inFile:
            #print(line)

            #entryPoint = entryPointConstructer(line)
            #print(entryPoint.pos)
            #if entryPoint.pos >= a.pos & entryPoint.pos < b.pos:
            #    print("IS!")
            #    out.write(entryPointLogConstructer(entryPoint))


#entryPoint_A = entryPointConstructer("1; 28; TRUE; 32")

#pInRoomLister()
#print(pInRoomList)

#pInRoomFiller()


rawDataFile.close()
outputFile.close()
print("Finish! Entry")
