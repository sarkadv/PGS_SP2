from enum import Enum


class Role(Enum):
    """
    Enum represents all the roles of entities that can be present in the input file.
    """

    FOREMAN = "FOREMAN"
    WORKER = "WORKER"
    LORRY = "LORRY"
    FERRY = "FERRY"
