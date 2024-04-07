import os.path
import sys

from line_parts import *
from xml_writer import *


def check_program_arguments():
    """
    Checks if arguments given to the program are valid.
    Correct format: python3 ./run_sp2.py -i <input file> -o <output file>
    :return: True if arguments valid / False otherwise
    """
    if len(sys.argv) != 5:
        return False

    if (sys.argv[1] != "-i") or (sys.argv[3] != "-o"):
        return False

    if not os.path.isfile(sys.argv[2]):  # checks if input file exists and is not a directory
        return False

    return True


def main():
    """
    Input function of the program.
    Checks whether arguments are valid and then proceeds to read the input file line by line.
    Each line is processed into a LineParts instance to gain information about time, role, ID, action
    and duration of the event.
    According to this information, methods of the Stats instance are called.
    The Stats instance is then given to the XMLWriter instance to create a XML file of the given format.
    :return: None
    """

    if not check_program_arguments():
        print("Wrong program arguments! Usage: python3 ./run_sp2.py -i <input file> -o <output file>")
        exit(1)

    input_file = sys.argv[2]
    output_file = sys.argv[4]

    stats = Stats()  # instance to store important statistics
    first_line = True

    with open(input_file) as file:
        for line in file:
            if first_line:  # we take the time from the first line to get the duration of the simulation
                line_parts = LineParts(line)
                stats.set_simulation_start(line_parts.get_epoch_time())
                first_line = False

            else:
                line_parts = LineParts(line)

                # worker events
                if line_parts.get_role() == Role.WORKER:
                    # worker has finished mining a block
                    if line_parts.get_action() == Action.BLOCK_MINED:
                        stats.add_mined_block(line_parts.get_duration_ms())

                    # worker has finished mining a resource
                    elif line_parts.get_action() == Action.RESOURCE_MINED:
                        stats.add_mined_resource(line_parts.get_id(), line_parts.get_duration_ms())

                # ferry events
                elif line_parts.get_role() == Role.FERRY:
                    # ferry was loaded and starts to sail
                    if line_parts.get_action() == Action.LOADED_AFTER:
                        stats.add_ferry_journey(line_parts.get_duration_ms())

                # lorry events
                elif line_parts.get_role() == Role.LORRY:
                    # lorry was loaded
                    if line_parts.get_action() == Action.LOADED_AFTER:
                        stats.add_lorry_loaded(line_parts.get_id(), line_parts.get_duration_ms())

                    # lorry has finished driving to the ferry or the target location
                    elif line_parts.get_action() == Action.DROVE_TO_FERRY or \
                            line_parts.get_action() == Action.DROVE_TO_TARGET_LOCATION:
                        stats.add_lorry_travelled(line_parts.get_id(), line_parts.get_duration_ms())

        # we take the time from the last line to get the duration of the simulation
        stats.set_simulation_end(line_parts.get_epoch_time())

    # write stats to XML file
    xml_writer = XMLWriter(stats)
    xml_writer.create_XML(output_file)


main()
