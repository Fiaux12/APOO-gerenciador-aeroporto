from enum import Enum

class EnumStatusVoo(Enum):
    PLANEJADO = "Planejado"
    CONFIRMADO = "Confirmado"
    EMBARQUE = "Embarque"
    EM_VOO = "Em Voo"
    FINALIZADO = "Finalizado"
    CANCELADO = "Cancelado"