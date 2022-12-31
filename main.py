import mathTools

# script, which takes the new log file format as an input and is a base to work on
# YY-MM-DD_HH:MM:SS_ACTION_VALUE
blockSeperator = "_"


class PointInTime:
    def __init__(self, raw_line: str):
        self.rawLine = raw_line

    def get_day(self):
        day = self.rawLine.split(blockSeperator)[0].split("-")[2]
        return mathTools.leading_zero_remover(day)

    def get_hour(self):
        hour = self.rawLine.split(blockSeperator)[1].split(":")[0]
        return mathTools.leading_zero_remover(hour)

    def get_minute(self):
        minute = self.rawLine.split(blockSeperator)[1].split(":")[1]
        return mathTools.leading_zero_remover(minute)

    def get_second(self):
        second = self.rawLine.split(blockSeperator)[1].split(":")[2]
        return mathTools.leading_zero_remover(second)

    def get_time_ident(self):
        full_date = self.rawLine.split(blockSeperator)[0].replace("-", "")
        full_time = self.rawLine.split(blockSeperator)[1].replace(":", "")
        time_ident = f"{full_date}{full_time}"
        return int(time_ident)


class PersonInRoom(PointInTime):
    def __init__(self, raw_line: str):
        super().__init__(raw_line)

def