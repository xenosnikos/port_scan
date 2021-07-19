from enum import Enum

from helpers.mongo_connection import db

class PortScanEnum(Enum):
    quick = 1
    regular = 2
    full = 3
