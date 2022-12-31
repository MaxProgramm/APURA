# YY-MM-DD_HH:MM:SS_ACTION_VALUE
blockSeperator = "_"



def scan_protokoll(protokoll_file_name: str):
    temperatur = 0.0
    person_in_room = False
    date = ""
    time = ""

    events = {
        "temperatur": temperatur,
        "pInRoom": person_in_room
        # Add events here!
    }

    boolTrans = {
        "True": True,
        "False": False
    }

    with open(protokoll_file_name) as protokoll:
        for line in protokoll:
            line = line.split(blockSeperator)
            date = line[0]
            time = line[1]
            if events[line[2]] == person_in_room:
                person_in_room = boolTrans[line[2]]

