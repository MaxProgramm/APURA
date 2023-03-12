import mathTools
from datetime import datetime
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
        # self.date = line[0]
        # self.time = line[1]
        self.date = datetime.now().strftime("%Y.%m.%d %H:%M:%S").split(" ")[0]
        self.time = datetime.now().strftime("%Y.%m.%d %H:%M:%S").split(" ")[1]
        self.absoluteTime = timeToSecondConverter(self.date, self.time)

class case:
    def __init__(self, wait_time: int, name: str, advice: str):
        self.waitTimeMinute = wait_time
        self.running = False
        # self.max_temp1 = max_temp1
        self.name = name
        self.advice = advice
        self.alarm_was_raised = False

    def send_mail(self):
        print("SEND MAIL!")
        pass

    def raise_alarm(self, marked: ProtokollLine, end: ProtokollLine):
        print(f"{self.name} | {marked.date} {marked.time} -> {end.date} {end.time} | Time -minutes-: {((end.absoluteTime - marked.absoluteTime) / 60).__int__()} | {self.advice}")

    def raise_live_alarm(self, diff):
        if not self.alarm_was_raised:
            self.send_mail()
            self.alarm_was_raised = True
        print(f"{self.name} | {diff}s")

    def live_check(self):
        if self.running:
            date = datetime.now().strftime("%Y.%m.%d %H:%M:%S").split(" ")[0]
            time = datetime.now().strftime("%Y.%m.%d %H:%M:%S").split(" ")[1]

            print(date, time)

            current_absolute_time = timeToSecondConverter(date, time)
            diff = current_absolute_time - self.marked.absoluteTime

            if diff > self.waitTimeMinute * 60:
                self.raise_live_alarm(diff)
                return [True, f"{self.name} | {diff}s"]
        self.alarm_was_raised = False
        return [False, ""]

    def check(self, line: ProtokollLine):
        if line.pInRoom == False and line.temp1 > self.max_temp1:
            if self.running == False:
                self.marked = line
                self.running = True
                # print(f"{self.name} - marked - {line.rawLine}")
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
                    # print(f"{self.name} - Broke - {line.rawLine}")


# Here are the cases, which will get checked.



class Case1(case):
    def __init__(self, wait_time: int = 30, max_temp1: int = 19):
        super().__init__(wait_time, "TEMPERATUR ALARM", "Schalte doch mal die Heizung ab, wenn du nicht im Raum bist.")
        self.max_temp1 = max_temp1

    def check(self, line: ProtokollLine):
        if line.pInRoom == False and line.temp1 > self.max_temp1:
            if self.running == False:
                self.marked = line
                self.running = True
                # print(f"{self.name} - marked - {line.rawLine}")
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
                    # print(f"{self.name} - Broke - {line.rawLine}")


class Case2(case):

    def __init__(self, wait_time:int = 30):
        super().__init__(wait_time, "STECKDOSEN ALARM", "Schalte doch mal das Gerät ab, das an der Steckdose hängt, wenn du aus dem Zimmer gehst.")

    def check(self, line: ProtokollLine):
        if line.pInRoom == False and line.power > 0.1:
            if self.running == False:
                self.marked = line
                self.running = True
                # print(f"{self.name} - marked - {line.rawLine}")
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
                    # print(f"{self.name} - Broke - {line.rawLine}")



# Opens protokoll and goes through lines
print("finish")
