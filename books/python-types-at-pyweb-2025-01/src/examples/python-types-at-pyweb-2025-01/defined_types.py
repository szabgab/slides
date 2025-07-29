from typing import Literal
LevelType = Literal["debug", "info", "warning"]

size: LevelType = "debug"
#size = "error"

# ------------------------------------------

from datetime import datetime
from typing import TypedDict
HistoryType = TypedDict('HistoryType', {
    "date" : datetime,
    "level": LevelType,
    "text": str,
})

event: HistoryType = {
        "date": datetime.now(),
        "level": "debug",
        "text": "Demo typing",
}


