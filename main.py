import mathTools
protokoll_name = "rawData.txt"
splitter = " "

# Converts the 2022.12.30 08:40:26 date/time format to seconds, to be able to easily do comparisons
def timeToSecondConverter(date: str, time: str):
    years = mathTools.leading_zero_remover(date.split(".")[0])
    months = mathTools.leading_zero_remover(date.split(".")[1])
    days = mathTools.leading_zero_remover(date.split(".")[2])

    hours = mathTools.leading_zero_remover(time.split(":")[0])
    minutes = mathTools.leading_zero_remover(time.split(":")[1])
    seconds = mathTools.leading_zero_remover(time.split(":")[2])

    resultDate = (years * 31536000 + months * 2635 + days * 86400)
    resultTime = (hours * 3600 + minutes * 60 + seconds)
    return resultDate + resultTime

# Takes the string "on" or "off" as an input and returns a boolean. Used for the motion sensors log data
def StringBoolConverter(str_bool: str):
    table = {
        "on": True,
        "off": False
    }
    return table[str_bool]


# The class, which represents a line in the protokoll. Takes a protokoll line as an input and makes accessing the
# data more easily by converting it into the right format
class ProtokollLine:
    def __init__(self, line: str):
        line = line.replace("\n", "")
        self.rawLine = line
        line = line.split(splitter)
        self.eventType = line[2]
        self.pInRoom = StringBoolConverter(line[3])
        self.power = float(line[4])
        self.temp1 = float(line[5])
        self.temp2 = float(line[6])
        self.date = line[0]
        self.time = line[1]
        self.absoluteTime = timeToSecondConverter(self.date, self.time)


# Here are the cases, which will get checked.
class Case1:
    # checks if room temperature is above a specific value(19) while no one is in the room for a given amount of
    # minutes (standard 30 minutes)
    def __init__(self, wait_time: int = 30, max_temp1: int = 19):
        self.waitTimeMinute = wait_time
        self.running = False
        self.max_temp1 = max_temp1
        self.name = "TEMP ALARM"

    def raise_alarm(self, marked: ProtokollLine, end: ProtokollLine):
        print(f"{self.name} | {marked.time} -> {end.time} | Time -seconds-: {end.absoluteTime - marked.absoluteTime} | Time -minutes-: {(end.absoluteTime - marked.absoluteTime) / 60}")

    def check(self, line: ProtokollLine):
        if line.pInRoom == False and line.temp1 > self.max_temp1:
            if self.running == False:
                self.marked = line
                self.running = True
                #print(f"{self.name} - marked - {line.rawLine}")
                # print(line.rawLine)
            else:
                pass
        else:
            if self.running:
                if line.absoluteTime - self.marked.absoluteTime > (self.waitTimeMinute * 60):
                    # print(line.rawLine)
                    self.running = False
                    self.raise_alarm(self.marked, line)
                else:
                    self.running = False
                    #print(f"{self.name} - Broke - {line.rawLine}")


class Case2:
    # Checks if no one is in the room and the value of the Steckdose is over 0.0 power units for the given amount of
    # minutes
    def __init__(self, wait_time: int = 30):
        self.waitTimeMinute = wait_time
        self.running = False
        self.name = "PC ALARM"

    def raise_alarm(self, marked: ProtokollLine, end: ProtokollLine):
        print(f"{self.name} | {marked.time} -> {end.time} | Time -seconds-: {end.absoluteTime - marked.absoluteTime} | Time -minutes-: {(end.absoluteTime - marked.absoluteTime) / 60}")

    def check(self, line: ProtokollLine):
        if line.pInRoom == False and line.power > 0.1:
            if self.running == False:
                self.marked = line
                self.running = True
                #print(f"{self.name} - marked - {line.rawLine}")
                # print(line.rawLine)
            else:
                pass
        else:
            if self.running:
                if line.absoluteTime - self.marked.absoluteTime > (self.waitTimeMinute * 60):
                    # print(line.rawLine)
                    self.running = False
                    self.raise_alarm(self.marked, line)
                else:
                    self.running = False
                    #print(f"{self.name} - Broke - {line.rawLine}")


# Opens protokoll and goes through lines
with open(protokoll_name) as protokoll:
    print("opening protokoll file")
    c1 = Case1(30)
    c2 = Case2(1)
    for line in protokoll:
        # print(line)
        line = ProtokollLine(line)
        c1.check(line)
        c2.check(line)
        # print(line.rawLine)

    print("finish")
