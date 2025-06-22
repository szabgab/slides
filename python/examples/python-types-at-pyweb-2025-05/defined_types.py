from typing import Literal
LevelType = Literal["debug", "info", "warning", "error"]

size: LevelType = "debug"
#call it label size = "eror"

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


