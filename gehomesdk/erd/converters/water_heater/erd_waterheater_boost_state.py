from gehomesdk.erd.values import ErdWaterHeaterBoostModeState

from ..abstract import ErdReadWriteConverter
from ..primitives import *


class ErdWaterHeaterModeConverter(ErdReadWriteConverter[ErdWaterHeaterBoostModeState]):
    def erd_decode(self, value) -> ErdWaterHeaterBoostModeState:
        try:
            return ErdWaterHeaterBoostModeState(erd_decode_int(value))
        except ValueError:
            return ErdWaterHeaterBoostModeState.UNKNOWN

    def erd_encode(self, value: ErdWaterHeaterBoostModeState) -> str:
        return value.value
