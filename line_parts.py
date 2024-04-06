import calendar
import datetime

from role import *
from action import *


def get_date(string: str):
    date_parts = string.split("-")
    return int(date_parts[0]), int(date_parts[1]), int(date_parts[2])


def get_time(string: str):
    time_parts = string.split(":")
    seconds_parts = time_parts[2].split(".")
    return int(time_parts[0]), int(time_parts[1]), int(seconds_parts[0]), int(seconds_parts[1])


class LineParts:
    def __init__(self, line: str, separator):
        self.__epoch_time_ms = 0
        self.__role = None
        self.__id = 0
        self.__action = None
        self.__duration_ms = 0

        self.process_line(line, separator)

    def process_line(self, line: str, separator: str):
        parts = line.split(separator)

        datetime_parts = parts[0].split(" ")
        year, month, day = get_date(datetime_parts[0])
        hour, minute, second, millisecond = get_time(datetime_parts[1])

        datetime_object = datetime.datetime(year, month, day, hour, minute, second)
        epoch_time = (calendar.timegm(datetime_object.timetuple()) * 1000) + millisecond

        self.__epoch_time_ms = epoch_time

        role_index = [role.value for role in Role].index(parts[1])
        self.__role = list(Role)[role_index]

        self.__id = int(parts[2])

        action_list = list(Action)
        for i in range(len(action_list)):
            if action_list[i].value in parts[3]:
                self.__action = action_list[i]
                break

        if self.__action is not None:
            action_parts = parts[3].split(":")
            if len(action_parts) > 1:
                self.__duration_ms = int(action_parts[1].replace(" ", ""))

    def get_epoch_time(self):
        return self.__epoch_time_ms

    def get_role(self):
        return self.__role

    def get_id(self):
        return self.__id

    def get_action(self):
        return self.__action

    def get_duration_ms(self):
        return self.__duration_ms
