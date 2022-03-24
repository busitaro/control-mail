from concurrent.futures import ThreadPoolExecutor
from injector import Injector
from injector import inject

from data import Monitoring
from .daemon import check
from logic import Logic
from logic import LogicDiModule


executor = ThreadPoolExecutor(thread_name_prefix='thread')


class Start:
    @inject
    def __init__(self, logic: Logic):
        self.__logic = logic

    def start(self, monitoring: Monitoring):
        """
        処理を開始する

        Params
        -------
        monitoring: Monitoring
            監視設定オブジェクト
        """
        if self.__logic.daemonize:
            # デーモンスレッドの開始
            executor.submit(
                check,
                monitoring=monitoring,
                exec=self.__logic.exec
            )
        else:
            self.__logic.exec()


def start(monitoring: Monitoring, mode: str, daemonize: bool = False):
    """
    処理を開始する（エントリーポイント）

    Params
    -------
    monitoring: Monitoring
        監視設定オブジェクト
    daemonize: bool = False
        デーモンかするかどうかのフラグ
    """
    injector = Injector([LogicDiModule(mode, daemonize)])
    start = injector.get(Start)
    start.start(monitoring)
