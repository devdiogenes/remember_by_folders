import datetime
import json
import os

class RememberByTime:
    def __init__(self, message = "", scheduled_file = "./.remember_by_folders/self_scheduling.json"):
        self.__message = message 
        self.__now = datetime.datetime.now()
        self.__scheduled_file = scheduled_file
        self.__scheduled = self.__open_scheduled()

    def weekly(self, weekday = 0, time = "00:00"):

        self.time = datetime.datetime.strptime(time, "%H:%M")
        current_weekday = int(self.__now.strftime("%w"))
        days_to_next = ((weekday + 7) - current_weekday) % 7
        next_reminder = self.__now + datetime.timedelta(days = days_to_next)
    
        try: self.__scheduled["weekly"]
        except: self.__scheduled["weekly"] = {}
        try: self.__scheduled["weekly"][str(weekday)]
        except: self.__scheduled["weekly"][str(weekday)] = {}
        try: self.__scheduled["weekly"][str(weekday)][time]
        except: self.__scheduled["weekly"][str(weekday)][time] = self.__time_to_str(self.__now)

        next_scheduling = self.__str_to_time(self.__scheduled["weekly"][str(weekday)][time])

        if self.__now >= next_scheduling:
            os.mkdir(self.__message)
            self.__scheduled["weekly"][str(weekday)][time] = self.__time_to_str(next_reminder, "%Y-%m-%d ") + time

        self.__save_scheduled()

    def __open_scheduled(self):
        try: 
            open_schenduled_file = open(self.__scheduled_file)
            scheduled = json.loads(open_schenduled_file.read())
            open_schenduled_file.close()
            return scheduled
        except: 
            self.__scheduled = {}
            self.__save_scheduled()
            return {}

    def __save_scheduled(self):
        open_schenduled_file = open(self.__scheduled_file, "w")
        json.dump(self.__scheduled, open_schenduled_file, indent = 4)
        open_schenduled_file.close()

    def __str_to_time(self, string):
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M")

    def __time_to_str(self, string, time_format = "%Y-%m-%d %H:%M"):
        return datetime.datetime.strftime(string, time_format)