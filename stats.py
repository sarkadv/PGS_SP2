class Stats:
    def __init__(self):
        self.__simulation_start = 0
        self.__simulation_end = 0

        self.__total_blocks_mined = 0
        self.__total_resources_mined = 0
        self.__total_ferry_journies = 0
        self.__workers_resources_mined = dict()
        self.__workers_time_mined = dict()
        self.__lorries_time_loaded = dict()
        self.__lorries_time_travelled = dict()

        self.__total_time_blocks_mined = 0
        self.__total_time_resources_mined = 0
        self.__total_time_ferry_waited = 0

    def set_simulation_start(self, time_ms: int):
        self.__simulation_start = time_ms

    def set_simulation_end(self, time_ms: int):
        self.__simulation_end = time_ms

    def add_mined_block(self, time_ms: int):
        self.__total_blocks_mined += 1
        self.__total_time_blocks_mined += time_ms

    def add_mined_resource(self, worker_id: int, time_ms: int):
        self.__total_resources_mined += 1
        self.__total_time_resources_mined += time_ms

        self.__workers_resources_mined[worker_id] = self.__workers_resources_mined.get(worker_id, 0) + 1
        self.__workers_time_mined[worker_id] = self.__workers_time_mined.get(worker_id, 0) + time_ms

    def add_ferry_journey(self, time_waited_ms: int):
        self.__total_ferry_journies += 1
        self.__total_time_ferry_waited += time_waited_ms

    def add_lorry_loaded(self, lorry_id: int, time_ms: int):
        self.__lorries_time_loaded[lorry_id] = self.__lorries_time_loaded.get(lorry_id, 0) + time_ms

    def add_lorry_travelled(self, lorry_id: int, time_ms: int):
        self.__lorries_time_travelled[lorry_id] = self.__lorries_time_travelled.get(lorry_id, 0) + time_ms

    def get_total_blocks_mined(self):
        return self.__total_blocks_mined

    def get_total_average_time_blocks_mined(self):
        return round(self.__total_time_blocks_mined / self.__total_blocks_mined)

    def get_total_resources_mined(self):
        return self.__total_resources_mined

    def get_total_average_time_resources_mined(self):
        return round(self.__total_time_resources_mined / self.__total_resources_mined)

    def get_total_ferry_journies(self):
        return self.__total_ferry_journies

    def get_total_average_time_ferry_waited(self):
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
        return self.__simulation_end - self.__simulation_start
        