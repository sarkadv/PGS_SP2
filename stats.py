class Stats:
    """
    Class for storing information of interest about the simulation.
    """

    def __init__(self):
        """
        Constructor of the Stats class.
        """

        self.__simulation_start = 0
        """ start of the simulation in epoch time [ms] """

        self.__simulation_end = 0
        """ end of the simulation in epoch time [ms] """

        self.__total_blocks_mined = 0
        """ sum of blocks mined by every worker during the entire simulation """

        self.__total_resources_mined = 0
        """ sum of resources mined by every worker during the entire simulation """

        self.__total_ferry_journies = 0
        """ total ferry journies during the entire simulation """

        self.__workers_resources_mined = dict()
        """ dictionary of keys representing worker ID and values represeting the number of resources mined """

        self.__workers_time_mined = dict()
        """ dictionary of keys representing worker ID and values represeting the time the worker has mined """

        self.__lorries_time_loaded = dict()
        """ dictionary of keys representing lorry ID 
        and values represeting the time the lorry has waited for loading """

        self.__lorries_time_travelled = dict()
        """ dictionary of keys representing lorry ID and values represeting the time 
        the lorry has travelled (mine to ferry and ferry to target location) """

        # secondary variables
        self.__total_time_blocks_mined = 0
        """ sum of time blocks have been mined by every worker during the entire simulation """

        self.__total_time_resources_mined = 0
        """ sum of time resources have been mined by every worker during the entire simulation """

        self.__total_time_ferry_waited = 0
        """ sum of time the ferry has been waiting during the entire simulation """

    def set_simulation_start(self, time_ms: int):
        """
        Sets the time when the simulation has started.
        :param time_ms: epoch time the simulation has started [ms]
        :return: None
        """

        self.__simulation_start = time_ms

    def set_simulation_end(self, time_ms: int):
        """
        Sets the time when the simulation ended.
        :param time_ms: epoch time the simulation ended [ms]
        :return: None
        """

        self.__simulation_end = time_ms

    def add_mined_block(self, time_ms: int):
        """
        Increments the total blocks mined attribute by 1.
        Increments the total time blocks mined attribute by time duration [ms].
        :param time_ms: duration of block mining [ms]
        :return: None
        """

        self.__total_blocks_mined += 1
        self.__total_time_blocks_mined += time_ms

    def add_mined_resource(self, worker_id: int, time_ms: int):
        """
        Increments the total resources mined attribute by 1.
        Increments the total time resources mined attribute by time duration [ms].
        Increments the number of resources mined for this worker.
        Increments the time this worker has mined for by time duration [ms]
        :param worker_id: ID of the worker that mined the resource
        :param time_ms: duration of block mining [ms]
        :return: None
        """

        self.__total_resources_mined += 1
        self.__total_time_resources_mined += time_ms

        self.__workers_resources_mined[worker_id] = self.__workers_resources_mined.get(worker_id, 0) + 1
        self.__workers_time_mined[worker_id] = self.__workers_time_mined.get(worker_id, 0) + time_ms

    def add_ferry_journey(self, time_ms: int):
        """
        Increments the total ferry journies attribute by 1.
        Increments the time ferry has waited for by time duration [ms].
        :param time_ms: duration of the ferry wait
        :return:
        """

        self.__total_ferry_journies += 1
        self.__total_time_ferry_waited += time_ms

    def add_lorry_loaded(self, lorry_id: int, time_ms: int):
        """
        Sets the time lorry has waited for loading by time duration [ms].
        :param lorry_id: ID of the lorry that has finished loading
        :param time_ms: duration of the wait
        :return:
        """

        self.__lorries_time_loaded[lorry_id] = time_ms

    def add_lorry_travelled(self, lorry_id: int, time_ms: int):
        """
        Increments the time lorry has travlelled for by time duration [ms].
        :param lorry_id: ID of the lorry that was travelling
        :param time_ms: duration of the journey
        :return:
        """
        self.__lorries_time_travelled[lorry_id] = self.__lorries_time_travelled.get(lorry_id, 0) + time_ms

    # GETTERS
    def get_total_blocks_mined(self):
        return self.__total_blocks_mined

    def get_total_average_time_blocks_mined(self):
        # compute average by (total time / occurences) and rounding to the nearest integer
        return round(self.__total_time_blocks_mined / self.__total_blocks_mined)

    def get_total_resources_mined(self):
        return self.__total_resources_mined

    def get_total_average_time_resources_mined(self):
        # compute average by (total time / occurences) and rounding to the nearest integer
        return round(self.__total_time_resources_mined / self.__total_resources_mined)

    def get_total_ferry_journies(self):
        return self.__total_ferry_journies

    def get_total_average_time_ferry_waited(self):
        # compute average by (total time / occurences) and rounding to the nearest integer
        return round(self.__total_time_ferry_waited / self.__total_ferry_journies)

    def get_workers_resources_mined(self):
        return self.__workers_resources_mined

    def get_workers_time_mined(self):
        return self.__workers_time_mined

    def get_lorries_time_loaded(self):
        return self.__lorries_time_loaded

    def get_lorries_time_travelled(self):
        return self.__lorries_time_travelled

    def get_simulation_duration(self):
        # compute duration by substracting the start of the simulation from the end
        return self.__simulation_end - self.__simulation_start
        