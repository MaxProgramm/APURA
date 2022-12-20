import matplotlib.pyplot as plt
import numpy as np
import cleanEntryV3

rawDataFile = "output.txt"
outputFile = ""

arraysToPlot = []

xPoints = []
yPointsTemperatur = []

with open(rawDataFile) as file:
    for line in file:
        if str(line) == "\n":
            continue
        entryPoint = cleanEntryV3.entryPointConstructer(line)
        xPoints.append(entryPoint.pos)
        yPointsTemperatur.append(entryPoint.temp)


def getNumberOfLinesFile(fileName: str, skipClear=False):
    counter = 0
    with open(fileName) as file:
        for line in file:
            if skipClear and line == "\n":
                continue
            counter = counter + 1
    return counter


def roomPointer(fileName=rawDataFile):
    pInRoomPacks = [[]]

    pNotInRoomPacks = []
    firstFinished = False

    with open(fileName) as file:

        fileLineNumber = getNumberOfLinesFile(rawDataFile, True)
        currentLineNumber = 0

        for line in file:
            if str(line) == "\n":
                continue

            if firstFinished:
                print("DEBUG: " + line)
                epB = cleanEntryV3.entryPointConstructer(line)

                if epA.pInRoom and epB.pInRoom:
                    pInRoomPacks[len(pInRoomPacks) - 1].append(epA.pos)

                if epA.pInRoom and epB.pInRoom != True:
                    pInRoomPacks[len(pInRoomPacks) - 1].append(epA.pos)
                    pNotInRoomPacks.append([])
                    #ilesPInRoom.append([])

                if epA.pInRoom != True and epB.pInRoom:
                    pNotInRoomPacks[len(pNotInRoomPacks) - 1].append(epA.pos)
                    pInRoomPacks.append([])

                if epA.pInRoom != True and epB.pInRoom != True:
                    pNotInRoomPacks[len(pInRoomPacks) - 1].append(epA.pos)

                epA = epB

                # print("DEBUG: Current line number: " + str(currentLineNumber) + " | fileLineNumber: " + str(fileLineNumber))

                if currentLineNumber + 1 == fileLineNumber:
                    print("Last line")
                    if epB.pInRoom:
                        print("In room")
                        pInRoomPacks[len(pInRoomPacks) - 1].append(epB.pos)

                    if not epB.pInRoom:
                        print("Not in room")
                        pNotInRoomPacks[len(pNotInRoomPacks) - 1].append(epB.pos)

            else:
                epA = cleanEntryV3.entryPointConstructer(line)
                firstFinished = True
            currentLineNumber = currentLineNumber + 1

    return pInRoomPacks, pNotInRoomPacks


def makePointerVisible(pInRoomPacks, pNotInRoomPacks):
    for pack in pInRoomPacks:
        pack.append(pack[len(pack) - 1] + 1)
    for pack in pNotInRoomPacks:
        pack.append(pack[len(pack) - 1] + 1)

    return pInRoomPacks, pNotInRoomPacks


roomIn, roomNot = roomPointer(rawDataFile)
print(roomIn, roomNot)

roomIn, roomNot = makePointerVisible(roomIn, roomNot)
print(roomIn, roomNot)

for pack in roomIn:
    yPoints = []
    for point in pack:
        yPoints.append(1)
    plt.plot(np.array(pack), np.array(yPoints), color="green", linewidth="5.0")

for pack in roomNot:
    yPoints = []
    for point in pack:
        yPoints.append(1)
    plt.plot(np.array(pack), np.array(yPoints), color="red", linewidth="5.0")


xPointsArray = np.array(xPoints)
yPointsArrayTemperatur = np.array(yPointsTemperatur)


# Plotting
plt.plot(xPointsArray, yPointsArrayTemperatur)


plt.show()
