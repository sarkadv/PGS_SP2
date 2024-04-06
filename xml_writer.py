from xml.dom import minidom

from stats import *


class XMLWriter:
    def __init__(self, stats: Stats):
        self.__stats = stats

    def create_XML(self, output_file: str):
        root = minidom.Document()

        simulation = root.createElement("Simulation")
        simulation.setAttribute("duration", str(self.__stats.get_simulation_duration()))
        root.appendChild(simulation)

        self.create_XML_block_average_duration(root, simulation)
        self.create_XML_resource_average_duration(root, simulation)
        self.create_XML_ferry_average_wait(root, simulation)

        self.create_XML_workers(root, simulation)
        self.create_XML_vehicles(root, simulation)

        xml_indents = root.toprettyxml(indent="\t", encoding="utf-8")

        with open(output_file, "wb") as file:
            file.write(xml_indents)

    def create_XML_block_average_duration(self, root, parent):
        block_average_duration = root.createElement("blockAverageDuration")
        block_average_duration.setAttribute("totalCount", str(self.__stats.get_total_blocks_mined()))
        parent.appendChild(block_average_duration)

        block_average_duration_text = root.createTextNode(str(self.__stats.get_total_average_time_blocks_mined()))
        block_average_duration.appendChild(block_average_duration_text)

    def create_XML_resource_average_duration(self, root, parent):
        resource_average_duration = root.createElement("resourceAverageDuration")
        resource_average_duration.setAttribute("totalCount", str(self.__stats.get_total_resources_mined()))
        parent.appendChild(resource_average_duration)

        resource_average_duration_text = root.createTextNode(str(self.__stats.get_total_average_time_resources_mined()))
        resource_average_duration.appendChild(resource_average_duration_text)

    def create_XML_ferry_average_wait(self, root, parent):
        ferry_average_wait = root.createElement("ferryAverageWait")
        ferry_average_wait.setAttribute("trips", str(self.__stats.get_total_ferry_journies()))
        parent.appendChild(ferry_average_wait)

        ferry_average_wait_text = root.createTextNode(str(self.__stats.get_total_average_time_ferry_waited()))
        ferry_average_wait.appendChild(ferry_average_wait_text)

    def create_XML_workers(self, root, parent):
        workers = root.createElement("Workers")
        parent.appendChild(workers)

        workers_resources_mined = sorted(self.__stats.get_workers_resources_mined().items())
        workers_time_mined = self.__stats.get_workers_time_mined()

        for i in range(len(workers_resources_mined)):
            worker_id = workers_resources_mined[i][0]

            worker = root.createElement("Worker")
            worker.setAttribute("id", str(worker_id))
            workers.appendChild(worker)

            worker_resources = root.createElement("resources")
            worker.appendChild(worker_resources)

            worker_resources_text = root.createTextNode(str(workers_resources_mined[i][1]))
            worker_resources.appendChild(worker_resources_text)

            worker_duration = root.createElement("workDuration")
            worker.appendChild(worker_duration)

            worker_duration_text = root.createTextNode(str(workers_time_mined[worker_id]))
            worker_duration.appendChild(worker_duration_text)

    def create_XML_vehicles(self, root, parent):
        vehicles = root.createElement("Vehicles")
        parent.appendChild(vehicles)

        vehicles_time_loaded = sorted(self.__stats.get_lorries_time_loaded().items())
        vehicles_time_travelled = self.__stats.get_lorries_time_travelled()

        for i in range(len(vehicles_time_loaded)):
            vehicle_id = vehicles_time_loaded[i][0]

            vehicle = root.createElement("Vehicle")
            vehicle.setAttribute("id", str(vehicle_id))
            vehicles.appendChild(vehicle)

            vehicle_load_time = root.createElement("loadTime")
            vehicle.appendChild(vehicle_load_time)

            vehicle_load_time_text = root.createTextNode(str(vehicles_time_loaded[i][1]))
            vehicle_load_time.appendChild(vehicle_load_time_text)

            vehicle_transport_time = root.createElement("transportTime")
            vehicle.appendChild(vehicle_transport_time)

            vehicle_transport_time_text = root.createTextNode(str(vehicles_time_travelled[vehicle_id]
                                                                  + self.__stats.get_total_average_time_ferry_waited()))
            vehicle_transport_time.appendChild(vehicle_transport_time_text)
