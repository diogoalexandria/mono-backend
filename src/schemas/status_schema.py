from sqlalchemy.sql.sqltypes import Enum

class StatusOptions(str, Enum):
    active = "active"
    deactivated = "deactivated"