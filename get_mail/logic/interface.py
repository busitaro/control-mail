from abc import ABCMeta
from abc import abstractmethod

from ..data import Monitoring


class Logic(metaclass=ABCMeta):
    @abstractmethod
    def exec(self, monitoring: Monitoring):
        raise NotImplementedError()

    @abstractmethod
    def daemonize(self) -> bool:
        raise NotImplementedError()
