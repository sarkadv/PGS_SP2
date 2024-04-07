from enum import Enum


class Action(Enum):
    """
    Enum represents all actions of interest caused by entities in the input file.
    """

    BLOCK_MINED = "block mined"
    RESOURCE_MINED = "resource mined"
    LOADED_AFTER = "loaded after"
    DROVE_TO_FERRY = "drove to ferry"
    DROVE_TO_TARGET_LOCATION = "drove to target location"
