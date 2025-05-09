import enum
from typing import Optional


@enum.unique
class ErdWaterHeaterActiveControl(enum.Enum):
    OFF = 0
    ON = 1
    UNKNOWN = -1

    def stringify(self, **kwargs) -> Optional[str]:
        if self == ErdWaterHeaterActiveControl.UNKNOWN:
            return None
        return self.name.title()