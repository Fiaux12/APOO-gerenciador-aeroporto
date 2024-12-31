from enum import Enum

class EnumStatusVoo(Enum):
    PLANEJADO = "Planejado"
    CONFIRMADO = "Confirmado"
    CHECKIN_ABERTO = "Check-in Aberto"
    EMBARQUE = "Embarque"
    EM_VOO = "Em Voo"
    FINALIZADO = "Finalizado"
    CANCELADO = "Cancelado"