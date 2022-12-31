import mathTools
from enum import Enum

# YY-MM-DD_HH:MM:SS_ACTION_VALUE


blockSeperator = "_"

temp = 0
PersonInRoom = False



class PointInTime:
    class Events(Enum):
        temperatur = 1
        PersonInRoom = 2
        # Weitere Events hier einfügen

    eventNameTranslator = {
        "temperatur": Events.temperatur
        "PersonInRoom": Events.PersonInRoom
    }

    eventValueTranslator = {
        "True": True,
        "False": False
    }

    def create_event(self, event_name, raw_value):
        event = self.eventNameTranslator[event_name]
        if event == self.Events.PersonInRoom:
            value = self.eventValueTranslator[raw_value]
        if event == self.Events.temperatur:
            value = float(raw_value)
        else:
            print("Event not programmed")

        return [event, value]

    def __init__(self, raw_line: str):
        self.rawLine = raw_line
        self.event = self.create_event()


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



def do_stuff(protokoll_filename: str):
    with open(protokoll_filename) as protokoll:
        for line in protokoll:
            events[line.split("_")[2]] = line.split("3")





def compare(zeitpunkt_a, zeitpunkt_b, **kwargs):
    pass