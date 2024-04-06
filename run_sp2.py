import os.path
import sys

from line_parts import *
from xml_writer import *

SEPARATOR = "|"


def check_program_arguments():
    if len(sys.argv) != 5:
        return False

    if (sys.argv[1] != "-i") or (sys.argv[3] != "-o"):
        return False

    if not os.path.isfile(sys.argv[2]):
        return False

    return True


if __name__ == "__main__":
    if not check_program_arguments():
        print("Wrong program arguments! Usage: python3 ./run_sp2.py -i <input file> -o <output file>")
        exit(1)

    input_file = sys.argv[2]
    output_file = sys.argv[4]

    stats = Stats()
    first_line = True

    with open(input_file) as file:
        for line in file:
            if first_line:
                line_parts = LineParts(line.rstrip().replace(" " + SEPARATOR + " ", SEPARATOR), SEPARATOR)
                stats.set_simulation_start(line_parts.get_epoch_time())
                first_line = False

            else:
                line_parts = LineParts(line.rstrip().replace(" " + SEPARATOR + " ", SEPARATOR), SEPARATOR)

                if line_parts.get_role() == Role.WORKER:
                    if line_parts.get_action() == Action.BLOCK_MINED:
                        stats.add_mined_block(line_parts.get_duration_ms())
                    elif line_parts.get_action() == Action.RESOURCE_MINED:
                        stats.add_mined_resource(line_parts.get_id(), line_parts.get_duration_ms())

                elif line_parts.get_role() == Role.FERRY:
                    if line_parts.get_action() == Action.LOADED_AFTER:
                        stats.add_ferry_journey(line_parts.get_duration_ms())

                elif line_parts.get_role() == Role.LORRY:
                    if line_parts.get_action() == Action.LOADED_AFTER:
                        stats.add_lorry_loaded(line_parts.get_id(), line_parts.get_duration_ms())
                    elif line_parts.get_action() == Action.DROVE_TO_FERRY or \
                            line_parts.get_action() == Action.DROVE_TO_TARGET_LOCATION:
                        stats.add_lorry_travelled(line_parts.get_id(), line_parts.get_duration_ms())

        stats.set_simulation_end(line_parts.get_epoch_time())

    xml_writer = XMLWriter(stats)
    xml_writer.create_XML(output_file)
