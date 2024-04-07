import calendar
import datetime

from role import *
from action import *

SEPARATOR = "|"     # separates information types in one line


def get_date_parts(string: str):
    """
    Gets year, month and day from a string.
    :param string: string in format Y-M-D.
    :return: integers of year, month and day
    """

    date_parts = string.split("-")
    return int(date_parts[0]), int(date_parts[1]), int(date_parts[2])


def get_time_parts(string: str):
    """
    Gets hour, minute, second and millisecond from a string.
    :param string: string in format H:M:S.MS
    :return: integers of hour, minute, second and millisecond
    """

    time_parts = string.split(":")
    seconds_parts = time_parts[2].split(".")
    return int(time_parts[0]), int(time_parts[1]), int(seconds_parts[0]), int(seconds_parts[1])


class LineParts:
    """
    Class that stores information about time, role, ID, action and duration of an event.
    """

    def __init__(self, line: str):
        """
        Constructor of the LineParts class.
        :param line: string in format Y-M-D H:M:S.MS | ROLE | ID | action description: (duration in ms optional)
        """

        self.__epoch_time_ms = 0
        """ time of the event in milliseconds passed since 1.1. 1970 00:00:00 """

        self.__role = None
        """ role of the entity that caused this event (WORKER, LORRY, FERRY) """

        self.__id = 0
        """ ID of the entity that caused this event """

        self.__action = None
        """ description of the action caused by entity """

        self.__duration_ms = 0
        """ duration of the event in milliseconds (optional) """

        self.process_line(line)

    def process_line(self, line: str):
        """
        Method called by the constructor.
        Separates line into information about time, role, ID, action and duration of an event.
        :param line: string in format Y-M-D H:M:S.MS | ROLE | ID | action description: (duration in ms optional)
        :return: None
        """

        # line split by SEPARATOR
        parts = line.rstrip().replace(" " + SEPARATOR + " ", SEPARATOR).split(SEPARATOR)

        datetime_parts = parts[0].split(" ")
        year, month, day = get_date_parts(datetime_parts[0])
        hour, minute, second, millisecond = get_time_parts(datetime_parts[1])

        datetime_object = datetime.datetime(year, month, day, hour, minute, second)

        # multiply by 1000 to get milliseconds from seconds
        epoch_time = (calendar.timegm(datetime_object.timetuple()) * 1000) + millisecond

        self.__epoch_time_ms = epoch_time

        role_index = [role.value for role in Role].index(parts[1])
        self.__role = list(Role)[role_index]    # role is a Role enum

        self.__id = int(parts[2])

        action_list = list(Action)
        for i in range(len(action_list)):
            if action_list[i].value in parts[3]:
                self.__action = action_list[i]  # action is an Action enum
                break

        if self.__action is not None:
            action_parts = parts[3].split(":")
            if len(action_parts) > 1:   # duration of the action was also given
                self.__duration_ms = int(action_parts[1].replace(" ", ""))

    # GETTERS
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
