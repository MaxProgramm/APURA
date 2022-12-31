protokoll_name = "rawData.txt"
splitter = " "

def StringBoolConverter(str_bool: str):
    table = {
        "on": True,
        "off": False
    }
    return table[str_bool]

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
        self.absoluteTime = int(f"{line[0].replace('.', '')}{line[1].replace(':', '')}")
        self.date = line[0]
        self.time = line[1]

def raise_alarm(marked: ProtokollLine, end: ProtokollLine):
    print(f"{marked.time} -> {end.time} | Time -seconds-: {end.absoluteTime - marked.absoluteTime} | Time -minutes-: {(end.absoluteTime - marked.absoluteTime) / 60}")


class Case1:
    def __init__(self, wait_time: int, max_temp1: int = 19):
        self.waitTimeMinute = wait_time
        self.running = False
        self.max_temp1 = max_temp1

    def check(self, line: ProtokollLine):
        if line.pInRoom == False and line.temp1 > self.max_temp1:
            if self.running == False:
                self.marked = line
                self.running = True
                print(f"marked - {line.rawLine}")
                # print(line.rawLine)
            else:
                pass
        else:
            if self.running:
                if line.absoluteTime - self.marked.absoluteTime > (self.waitTimeMinute * 60):
                    # print(line.rawLine)
                    self.running = False
                    raise_alarm(self.marked, line)
                else:
                    self.running = False
                    print(f"Broke - {line.rawLine}")


class Case2:
    pass



with open(protokoll_name) as protokoll:
    print("opening protokoll file")
    c1 = Case1(30)
    for line in protokoll:
        #print(line)
        line = ProtokollLine(line)
        c1.check(line)
        #print(line.rawLine)


    print("finish")

