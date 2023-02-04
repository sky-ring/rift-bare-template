from rift import *


class BaseContract(Contract):
    def internal_receive(self) -> None:
        pass

    def external_receive(self) -> None:
        pass
